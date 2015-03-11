# -*- coding: utf-8 -*-
import json
import threading
import time
import SocketServer
import re

messages = []
usernames = []

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """
    global messages
    global usernames
    
    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            print(received_string)
            #TODO: Add handling of received payload from client
            print(received_string)
     
         
    def process_data(self, data):
        decoded = json.loads(data)
        
        if decoded['request'] == 'login':
          self.login(decoded.get('username', '')) 

        if not self.logged_in:
            return
        
        if decoded['request'] == 'logout':
          self.logout()
          
        if decoded['request'] == 'message':
            if decoded.get("message", "") != "":
                padd=" "*(len(max(usernames, key=len))-len(self.username))
                message = self.timestamp()+padd+" %s| %s"%(self.username, decoded['message'])
                self.broadcast(message)
    
         
    def login(self, username):
        if(not re.match(r'^[A-Za-z0-9_]+$', username)):
            self.send({'response':'login', 'error':'Invalid username!', 'username':username}) 
            return
        if not username in usernames:
            self.username = username
            usernames.append(username)
            self.logged_in = True
            self.request.sendall({'response':'login', 'username':self.username})
            messages.append("*** " + self.username + " has joined the chat.")

        else:
            self.send({'response': 'login', 'error':'Name already taken!', 'username':username})
            
    
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations is necessary
    """
    allow_reuse_address = True #Statisk variabel

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations is necessary
    """
    HOST, PORT = '0.0.0.0', 9998
    print 'Server running...'
    
    #Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
    
 


