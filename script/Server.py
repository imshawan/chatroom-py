import threading
import socket
import os
import sys
from time import sleep

print('\n')
print('          ###############################')
print('          ###      D3V: iMSHAWAN      ###')
print('          ###############################\n\n')

def configure():
    h = input('Enter Host IP: ')
    host = "'%s'" % h
    port = input('Enter Port: ')
    with open('config.py','w') as writefile:
        writefile.write(f'hostname = {host}\nportID = {port}\n')
        print('Configured!\n')

if not os.path.isfile('config.py'):
    f = open('config.py', 'w')
with open('config.py','r') as f:
    read = f.readlines()
    if not read:
        print('Configure your Server ')
        configure()
    else:
        pass

import config
host = config.hostname
port = config.portID


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((host, port))
except OSError:
    print("Invalid Host IP address or port\n")
    input("Press any key to re-configure...")
    configure()
try:
    server.listen()
except OSError:
    print("Please Close and restart the Program\n")
    input("Press any key to continue...")
    sys.exit()
    

global clients 
global names
clients = []
names = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except OSError:
            pass
        
def TimeToKickSomeone(hisname):
    if hisname in names:
        namesIndexNumber = names.index(hisname)
        CliToKick = clients[namesIndexNumber]
        clients.remove(CliToKick)
        CliToKick.send('You have been kicked by the ADMIN'.encode('ascii'))
        CliToKick.close()
        names.remove(hisname)
        broadcast(f'{hisname} Was kicked by the ADMIN'.encode('ascii'))

def TimeToBanSomeone(ban_name):
    if ban_name in names:
        namesIndexNumber = names.index(ban_name)
        CliToBan = clients[namesIndexNumber]
        clients.remove(CliToBan)
        CliToBan.send('You have been BANNED by the ADMIN'.encode('ascii'))
        CliToBan.close()
        names.remove(ban_name)
        broadcast(f'{ban_name} Was BANNED by the ADMIN'.encode('ascii'))


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            message1 = message2 = message
            if message1.decode('ascii').startswith('KICK'):
                if names[clients.index(client)] == 'admin' or name == 'Admin' or name == 'ADMIN':
                    kick_usr = message1.decode('ascii')[5:]
                    TimeToKickSomeone(kick_usr)
                else:
                    client.send('Command was refused'.encode('ascii'))
            elif message1.decode('ascii').startswith('BAN'):
                print(message2)
                if names[clients.index(client)] == 'admin' or name == 'Admin' or name == 'ADMIN':
                    ban_usr = message2.decode('ascii')[4:]
                    TimeToBanSomeone(ban_usr)
                    with open('list.txt', 'a') as banlst:
                        banlst.write(f'{ban_usr}\n')
                    client.send(f'{ban_usr} was banned'.encode('ascii'))
                else:
                    client.send('Command was refused'.encode('ascii'))
            else:    
                broadcast(message)
        except:
            index = clients.index(client)
            client.close()
            try:
                name = names[index]
            except IndexError:
                pass
            broadcast(f'{name} left the chat'.encode('ascii'))
            names.remove(name)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
                # GET and APPEND the name from the client
        client.send('NICK'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        
        if not os.path.isfile('list.txt'):
            f = open('list.txt', 'w')
        with open('list.txt', 'r') as read:
            bannedUsers = read.readlines()

        if name +'\n' in bannedUsers:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        if name == 'admin' or name == 'Admin' or name == 'ADMIN':
            client.send('CODE'.encode('ascii'))
            paswd = client.recv(1024).decode('ascii')

            if paswd != '3496':
                client.send('DENIED'.encode('ascii'))
                client.close()
                continue
            

        names.append(name)
        clients.append(client)

        print(f'Name of the client is {name}')
        broadcast(f'{name} Joined the chat'.encode('ascii'))
        if name == 'admin' or name == 'Admin' or name == 'ADMIN':
            client.send(f'Connected to the ChatRoom as SuperUser/ADMIN!'.encode('ascii'))
        else:
            client.send(f'Connected to the ChatRoom as {name}'.encode('ascii'))
        client.send('Type message...'.encode('ascii'))
        # Starting the threads
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('1. Re-configure Server')
print('2. Start Server with pervious Configurations\n')
ans = input('Enter Selection...')
if ans == '1':
    configure()
    print("Please Close and restart the Program\n")
    input("Press any key to continue...")
    sys.exit()
if ans == '2':
    print('\nStarting up server...')
    sleep(1)
    print('Server started at port %s'%port)
    receive()
else:
    print('Invalid Choice')
