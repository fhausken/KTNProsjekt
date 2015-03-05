# -*- coding: utf-8 -*-
import socket

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # TODO: Finish init process with necessary code
        self.host=host
        self.server_port=server_port

    def run(self):
        # Initiate the connection to the server
        # hello 
        self.connection.connect((self.host, self.server_port))
        print("Connected")

    def disconnect(self):
        self.connection.close()

    def receive_message(self, message):
        # TODO: Handle incoming message
        self.connection

    def send_payload(self, data):
        self.connection.send("" + data)


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary.'localhost' 
    """
    client = Client('localhost', 9998)
    client.run()
<<<<<<< HEAD
    client.send_payload('Hei')
=======
    try:
        client.send_payload('Fredrik: ',"Hei")
        client.send_payload('Fredrik: ',"Jeg er keen på is")
    finally:
        
        client.disconnect()
        print("Socket is shutdown")
    
    
>>>>>>> master
