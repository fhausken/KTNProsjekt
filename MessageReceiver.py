# -*- coding: utf-8 -*-
from threading import Thread
import re

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and permits
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
    This method is executed when creating a new MessageReceiver object

        """
        t = Thread(target=self.take_input)
        t.setDaemon=True
        t.start()
        # Flag to run thread as a deamon
        self.daemon = True
<<<<<<< HEAD
        
=======
>>>>>>> Martin

        # TODO: Finish initialization of MessageReceiver

    def run(self):
        while True:
            #this thread stops here until it has data, so no need for time.sleep
            data = raw_input()
            command = re.findall("^[/]\w+", data)
            if command:
                if command[0] in self.commands:
                    self.commands[command[0]]()
                continue
            if data != "":
                self.send(self.parse({"request":"message", "message":data}))
