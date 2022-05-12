#--- server.py was alreagy given I changed it --- Modifier : Senjuti Dutta
#--- server.py is called through vobot.py to start server and get all the messages
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import time
import os
import urllib
import json
import codecs
import pprint
import requests
import lib.volbot

#-----changed-----#
#hostname = "localhost"
#serverPort = 8000

class BotServer(BaseHTTPRequestHandler):
    #BotServer that receives and responds to htpp requests and inherit BaseHTTPRequestHandler's class
    def __init__(self, DialogManager, *args):
        self. DialogManager = DialogManager
        BaseHTTPRequestHandler.__init__(self, *args)
    def _set_headers(self):
        # WARNING: DO NOT TOUCH THIS CODE!
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.end_headers()

    def do_HEAD(self):
        # WARNING: DO NOT TOUCH THIS CODE!
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()

        # A dummy list of recommendations and similarity scores.
        self.wfile.write(bytes(json.dumps({'hello': 'world', 'received': 'ok'}), 'utf-8'))

    # POST echoes the message adding a JSON field
    def do_POST(self):
        # read the message and convert it into a python dictionary
        length = int(self.headers['Content-Length'])
        message = urllib.parse.parse_qs(self.rfile.read(length), keep_blank_values=1)
        print(message)

        # Print out what we've received.
        print('-: "NEW MESSAGE :-')
        t = message[b'type'][0].decode('utf-8')
        u = message[b'user'][0].decode('utf-8')

        #if t == 'reactive': # Reactive messages are chat messages.
        #print('msg: ' + message[b'msg'][0].decode('utf-8'))
        respMsg = self.DialogManager.handle_msg(message)





            # Simulate a response with a hard coded dictionary.

            #respMsg = {
                #'user' : 'Sam',
                #'msg': 'This is a test response for reactive messages.'
            #}

        #else:
            # Note: Proactive "messages" have no msg component, and we therefore have nothing to print.

            # Simulate a response with a hard-coded dictionary.
            #respMsg = {
                #'user' : 'Sam',
                #'msg': '' # An empty 'msg' string tells the client UI that there are no proactive messages to handle.
            #}

        # send the message back
        self._set_headers()
        self.wfile.write(bytes(json.dumps(respMsg), 'utf-8'))
        #a = mn.DialogManager(state = 'abc', dialogs = message)
