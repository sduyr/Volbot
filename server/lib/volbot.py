#---- Author: Senjuti Dutta---
# Volbot framework takes botname, manager and dialogs where validate_dialogs checks the structure 
import sys
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import lib.server
import lib.manager



class VolBot():
    # volbot class that can be instantiated to create a web-hosted chatbot
    def __init__(self, name, manager, dialogs):
        # instance variables
        self.name = name
        # instantiate a dialog mananger
        self.manager = lib.manager.DialogManager(dialogs = dialogs,name = self.name)
        self.dialogs = dialogs

        def serverWrapper(*args):
            lib.server.BotServer(self.manager, *args)

        # instantiate and start serving an HTTP server
        self.server = HTTPServer(('localhost', 9738),serverWrapper)
        print("[SERVING] BotServer : http://%s:%s" % ('localhost', 9738))

        self.validate_dialogs()

        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass

        # close the server after we've hit a keyboard interrupt
        self.server.server_close()
        print("Server stopped.")





    # This instance method validates the structure of the dialogs
    def validate_dialogs(self):

        count = 0
        for i in self.dialogs.keys():
            flag = 0
            #if i in dialogs.keys():
            for j in self.dialogs[i].keys():
                # Checking all three keys default, type and waterfall
                if j == 'type':
                    if self.dialogs[i][j] == 'proactive' or self.dialogs[i][j] == 'reactive':
                        flag = 1
                elif j == 'default':
                    if self.dialogs[i][j] == True or self.dialogs[i][j] == False:
                        flag +=1
                elif j == 'waterfall':
                    if type(self.dialogs[i][j]) == list:
                        for s in self.dialogs[i][j]:
                            if type(s) == str:
                                flag1 = True
                        if flag1== True:
                            flag+=1
                        elif type(self.dialogs[i][j]) == str:
                            flag +=1

            # Checking if all three keys meet the mentioned requirements
            if flag == 3:
                count+=1
            #print (count)
        if count >= 1:
            return True
        else:
            # if dialog structure does not meet program halts
            sys.exit() # program halts









'''
        # instantiate and start serving an HTTP server
        self.server = HTTPServer(('localhost', 9738), lib.server.BotServer)
        print("[SERVING] BotServer : http://%s:%s" % ('localhost', 9738))

        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass

        # close the server after we've hit a keyboard interrupt
        self.server.server_close()
        print("Server stopped.")
'''
'''
class DialogManager:
    def__init__(self):
'''
