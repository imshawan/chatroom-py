# A Simple Chatroom

This is a Python program that enables us to set up a simple Chat Room server and allow multiple clients to connect to it using a client-server connection script. The code uses the concept of sockets and threading.

## Modules used

This program used modules namely as: socket, threading, time and from os I used system and name

# Usage

This server can be set up on a local area network by choosing any on computer to be a server node, and using that computer’s private IP address as the server IP address.
For example, if a local area network has a set of private IP addresses assigned ranging from 192.168.1.2 to 192.168.1.100, then any computer from these 99 nodes can act as a server, and the remaining nodes may connect to the server node by using the server’s private IP address. Care must be taken to choose a port that is currently not in usage. For example, port 22 is default for ssh, and port 80 is default for HTTP protocols. So these two ports preferably, shouldn't be used or reconfigured to make them free for usage.

### To run the script, simply clone my repo and run server.py
Then configure the server get your host IP address (ipv4) using ipconfig command with Command prompt or for Linux and Mac use terminal with ifconfig command. After that assign a port. For example if 192.168.43.34 is your IP than you can use ports such as 33434 or simply 33333

Then you can run the Client.py file and connect with the server with the IP and port assigned to the server.
