import threading
import socket
import time
from os import name, system

hostname = input("Enter Server Address: ")
#hostname = '192.168.43.3'
port = int(input("Enter PORT: "))
#port = 33333
print("Trying to connect to the server...")
time.sleep(1)
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

print('')
print('                                             #################')
print('                                             # D3V: iMSHAWAN #')
print('                                             #################')

nickname = input("Enter your Username/name: ")
if nickname == 'admin' or nickname == 'Admin' or nickname == 'ADMIN':
    paswd = input("Enter password for admin: ")
    
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((hostname, port))
count = False

def receive():
    while True:
        global count
        if count == True:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                nextstp = client.recv(1024).decode('ascii')
                if nextstp == 'CODE':
                    client.send(paswd.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'DENIED':
                        print("Connection was refused by the Server")
                        count = True
                elif nextstp == 'BAN':
                    print('Connection refused because of Ban')
                    client.close()
                    count = True
            else:
                print("                                         " + message)
        except:
            print('An error occurred!')
            client.close()
            break

def write():
    while True:
        if count == True:
            break
        message = f'{nickname}: {input("")}'
        if message[len(nickname)+2:].startswith('/'):
            if nickname == 'admin' or nickname == 'Admin' or nickname == 'ADMIN':
                if message[len(nickname)+2:].startswith('/kick'):
                    client.send(f'KICK {message[len(nickname)+2+6:]}'.encode('ascii'))
                elif message[len(nickname)+2:].startswith('/ban'):
                    client.send(f'BAN {message[len(nickname)+2+5:]}'.encode('ascii'))
            else:
                print("You don't have ADMIN Privilages!")
        else:
            try:
                client.send(message.encode('ascii'))
            except OSError:
                pass

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
