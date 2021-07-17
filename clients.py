from sys import argv
from socket import socket
from threading import Thread
from time import sleep
from quotes import Quotes

def main(args):
    """Main for clients"""
    try:
        number_of_clients = int(args[0])
    except:
        number_of_clients = 1
    quote = Quotes()
    for x in range(number_of_clients):
        number = x + 1
        my_thread = Thread(target=create_client, args=(number,))
        my_thread.start()

def create_client(number):
    """Create a client """
    new_socket = socket()
    new_socket.connect(('localhost',8000))
    for x in range(2):
        phrase = Quotes().random()
        message = f"{phrase[1]} - {phrase[0]}"
        print(f"\nClient {number} sent:\n{message}")
        new_socket.send(str.encode(message))
        sleep(1)
    new_socket.close()


if __name__=="__main__":
    main(argv[1:])
