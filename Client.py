# -*- coding: utf-8 -*-
import socket
import json
import threading
import re
import MessageReceiver

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
        print "Welcome to the bigtime chat!\nPlease specify server ip:port, or leave empty for the defaults "+host+":"+str(server_port)
        innInfo=raw_input('>')
        if innInfo :
            host=innInfo.split(":")[0]
            port=int(innInfo.split(":")[1])
            
        self.connection.connect((host, port))
        self.logged_in = False
        self.commands = {"/logout":self.disconnect}
        
        while not self.logged_in:
            self.username = raw_input('Username: ')
            self.send(self.parse({'request':'login', 'username':self.username}))
            response = self.connection.recv(1024).strip()
            self.process_json(response)
        
        #messagerece = MessageReceiver();
        #messagerece.__init__(self, )
        
        while self.logged_in:
            received_data = self.connection.recv(1024).strip()
            self.process_json(received_data)
        self.connection.close()
        
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
    
    def parse(self, data):
        return json.dumps(data)
    
    def process_json(self, data):
        index = 0
        while data.find("{", index) >= 0:
            start = data.find("{", index)
            end = data.find("}", start)
            index = end
            self.process_data(data[start:end+1])
    
    

if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations is necessary.'localhost' 
    """
    client = Client('localhost', 9998)
    client.run()
    client.send_payload('Hei')
    try:
        client.send_payload('Fredrik: ',"Hei")
        client.send_payload('Fredrik: ',"Jeg er keen på is")
    finally:
        
        client.disconnect()
        print("Socket is shutdown")
    
    
