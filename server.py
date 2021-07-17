from socket import socket
from threading import Thread
from sys import argv, exit
from multiprocessing import Process

new_socket = socket()
new_socket.bind(('localhost',8000))
new_socket.listen(10)

def main(args):
    """Main for server"""
    try:
        option = args[0]
    except:
        option = "multithread"
    option = str(option).capitalize()
    client = 0
    if option == "Multithread":
        while True:
            connection, address = new_socket.accept()
            client = client + 1
            my_thread = Thread(target=receive_connection, args=(option, connection, client))
            my_thread.start()
    else:
        while True:
            connection, address = new_socket.accept()
            client = client + 1
            my_process = Process(target=receive_connection, args=(option, connection, client))
            my_process.start()        

def receive_connection(option, connection, client):
    print(f"\n>> {option} server\n   receiving a new connection...")
    while True:
        response = connection.recv(1024)
        if response:
            print(f">> Client {client}\n{response}")
        else:
            exit()
    connection.close()

if __name__=="__main__":
    main(argv[1:])
