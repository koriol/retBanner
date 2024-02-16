#!/usr/bin/python

import socket
from termcolor import colored

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket()
        sock.connect((ip, port))
        banner = sock.recv(1024)
        # receives data on a socket with descriptor socket and stores it in a buffer
        # 1024 is the data limit of data that is received
        return banner
    except:
        return
    
def main():
    ip = input(colored("[+] Enter a Target IP: ", 'blue'))
    port = 80
    # for port in range(1,100):
    # ip = '192.168.1.220'
    banner = retBanner(ip, port)
    if banner:
            print(colored(f'[+] Port {str(port)} at host {ip} returns: {str(banner)}', 'green')) # + str(port) + ' at host ' + ip + " returns: " + str(banner)))
        

main()