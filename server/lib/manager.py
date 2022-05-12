#Author : ----Senjuti Dutta----#
#--- whenever anybot.py is run it will pass message through handle_msg instance method and it hamdles two different type of messages: proactive and reactive
import socketserver
import time
import os
import urllib
import json
import codecs
import sys
import lib.volbot
from datetime import datetime, timedelta



class DialogManager():
    def __init__(self, dialogs, name = ''):
        self.state = {'Sam':[], 'Amanda':[]}
        self.dialogs = dialogs
        #this list is used to store reminders
        self.reminder_queue=[]
        self.name = name


    #This method generates response handle two different type of requests
    def handle_msg(self, msg):
      # When the message type is reactive

        if msg[b'type'] == [b'reactive']:
            print('msg: ' + msg[b'msg'][0].decode('utf-8'))
                #parse_msg(string_message)
            #print('msg: ' + msg[b'msg'][0].decode('utf-8'))
            if msg[b'msg'] == [b'introduction']:
                    self.state[msg[b'user'][0].decode()].append(['introduction',0])
                    ans_dict = {
                        'user': msg[b'user'][0].decode() , 'msg': self.dialogs['introduction']['waterfall'][0]
                        }
                    #dumps the json object into an elemet
                    json_string = json.dumps(ans_dict)
                    #load the json to a string
                    response = json.loads(json_string)
                    return response



            elif msg[b'msg'] == [b'capture']:
                self.state[msg[b'user'][0].decode()].append(['capture',0])
                ans_dict = {
                    'user': msg[b'user'][0].decode() , 'msg': self.dialogs['capture']['waterfall'][0]
                    }
                #dumps the json object into an elemet
                json_string = json.dumps(ans_dict)
                #load the json to a string
                response = json.loads(json_string)
                return response


            elif msg[b'msg'] == [b'echo']:
                self.state[msg[b'user'][0].decode()].append(['echo',0])
                ans_dict = {
                    'user': msg[b'user'][0].decode() , 'msg': (self.dialogs['echo']['waterfall'][0] + msg[b'msg'][0].decode())
                    }
                #dumps the json object into an elemet
                json_string = json.dumps(ans_dict)
                #load the json to a string
                response = json.loads(json_string)
                return response

            else:
                if len(self.state[msg[b'user'][0].decode()]) > 0 :
                    self.state[msg[b'user'][0].decode()][-1][1] += 1
                    if msg[b'msg'][0].find(b'remind me to')!= -1:
                        #print(msg[b'msg'][0])
                        self.parse_msg(msg)
                    if self.state[msg[b'user'][0].decode()][-1][1] ==  len(self.dialogs[self.state[msg[b'user'][0].decode()][-1][0]]['waterfall']):
                        self.state[msg[b'user'][0].decode()].pop(-1)

                        if len(self.state[msg[b'user'][0].decode()]) > 0 :
                            ans_dict = {
                                'user': msg[b'user'][0].decode() , 'msg':self.dialogs[ self.state[msg[b'user'][0].decode()][-1][0] ]['waterfall'] [self.state[msg[b'user'][0].decode()][-1][1]]
                                }
                            #dumps the json object into an elemet
                            json_string = json.dumps(ans_dict)
                            #load the json to a string
                            response = json.loads(json_string)
                            return response
                        else:
                            for i in self.dialogs.keys():
                                if self.dialogs[i]['default']== True:
                                    #for j in range(len(self.dialogs[i]['waterfall'])):
                                    self.state[msg[b'user'][0].decode()].append([i,0])
                                    if self.name =='EchoBot':
                                        ans_dict = {
                                            'user': msg[b'user'][0].decode() , 'msg': (self.dialogs[i]['waterfall'][0]+msg[b'msg'][0].decode())
                                            }
                                    else:
                                        ans_dict = {
                                            'user': msg[b'user'][0].decode() , 'msg': self.dialogs[i]['waterfall'][0]
                                            }
                                    #dumps the json object into an elemet
                                    json_string = json.dumps(ans_dict)
                                    #load the json to a string
                                    response = json.loads(json_string)
                                    return response


                    else:
                        ans_dict = {
                            'user': msg[b'user'][0].decode() , 'msg':self.dialogs[ self.state[msg[b'user'][0].decode()][-1][0] ]['waterfall'] [self.state[msg[b'user'][0].decode()][-1][1]]
                            }
                        #dumps the json object into an elemet
                        json_string = json.dumps(ans_dict)
                        #load the json to a string
                        response = json.loads(json_string)
                        return response

                else:
                    for i in self.dialogs.keys():
                        if self.dialogs[i]['default']== True:
                            #for j in range(len(self.dialogs[i]['waterfall'])):
                            self.state[msg[b'user'][0].decode()].append([i,0])
                            print(self.name)
                            if self.name =='EchoBot':
                                ans_dict = {
                                    'user': msg[b'user'][0].decode() , 'msg': (self.dialogs[i]['waterfall'][0]+msg[b'msg'][0].decode())
                                    }

                            else:
                                ans_dict = {
                                    'user': msg[b'user'][0].decode() , 'msg': self.dialogs[i]['waterfall'][0]
                                    }
                            #dumps the json object into an elemet
                            json_string = json.dumps(ans_dict)
                            #load the json to a string
                            response = json.loads(json_string)
                            return response


        elif msg[b'type'] == [b'proactive']:
            # When the message type is proactive

            if len(self.reminder_queue)>0:
                for i in range(len(self.reminder_queue)):
                    time_split = msg[b'time'][0].decode()
                    current_time = datetime.strptime(time_split, "%H:%M:%S %p")
                    print("before if")
                    if current_time == self.reminder_queue[i][0]:
                        print("within if")
                        reply = {'user': 'Sam','msg':('Hey! here is your reminder to ' + self.reminder_queue[i][1])}
                        self.reminder_queue.pop(i)
                        return reply


            if msg[b'time']==[b'8:00:00 AM']:
                self.state[msg[b'user'][0].decode()].append(['work-start',0])
                ans_dict = {
                    'user': msg[b'user'][0].decode() , 'msg': self.dialogs['work-start']['waterfall'][0]
                    }
                #dumps the json object into an elemet
                json_string = json.dumps(ans_dict)
                #load the json to a string
                response = json.loads(json_string)
                return response


            elif msg[b'time']==[b'5:00:00 PM']:
                self.state[msg[b'user'][0].decode()].append(['work-end',0])
                ans_dict = {
                    'user': msg[b'user'][0].decode() , 'msg': self.dialogs['work-end']['waterfall'][0]
                    }
                #dumps the json object into an elemet
                json_string = json.dumps(ans_dict)
                #load the json to a string
                response = json.loads(json_string)
                return response




    #parse all incoming chat messages
    def parse_msg(self, msg):
        split_1 = str(msg[b'msg'][0]).split( "b" )
        #print(split_1)
        split_2 = split_1[1].split("remind me to ")
        #print(split_2)
        split_3 = split_2[1].split(" in ")
        #print(split_3)
        split_4 = split_3[1].split(" seconds")
        #print(split_4)
        task = split_3[0]
        print(task)
        task_time = split_4[0]
        print(task_time)
        #time_taken = datetime.strptime(task_time,"%S")
        print(msg[b'time'][0])
        time_split = msg[b'time'][0].decode()
        user_msg_time = datetime.strptime(time_split, "%H:%M:%S %p")
        set_time = user_msg_time+ timedelta(seconds = int(task_time))
        self.reminder_queue.append([set_time,task])
        #print(set_time)

            #return queue.pop(0)





    # use split function and find function










                # one after other messages will be here
               #stack.append()
               #parse_msg =








      #if self.dialog == type:


    #return {

    #}
