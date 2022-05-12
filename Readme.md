Name: Senjuti Dutta
#------Python Library----#
Python Library used : time, os, urllib, json, codecs, sys, datetime,pprint, requests

#--- Changes----#
I have changed the code in server.py, volbot.py and created manager.py, EchoBot.py, reminderbot.py and taskbot.py

#----Introducing the Microsoft Bot Framework----#
I am attching screenshot should include an example of Echobot echoing my first name.

#--- Developing VolBot Framework----#
    1. Implemented a BotServer class that receives and responds to HTTP requests using the mentioned way
    2. Implemented a VolBot class that can be instantiated to create a web-hosted chatbot using the mentioned details
    3. Implement a DialogManager class that manages dialog state and generates chat responses using mentioned details

#---- Creating Bots with VolBot framework-----#
  1. EchoBot: A chatbot that includes a single dialog that echoes your message
  2. ReminderBot: A chatbot that allows you to set reminders via messages
  3.TaskBot: A chatbot for task management that includes three dialogs: a. introduction, b. work-start and c. work-end and


# Run any bot.py
(like Echobot.py, reminderbot.py and taskbot.py)
Open two terminal windows. In one window, run "python 'the bot you want to run'.py" ( for example : EchoBot.py, reminderBot.py, taskbot.py)
In the other terminal window, run"python html_server.py". You should now be capable
of opening the VolBot interface by navigating to http://localhost:8080/ in your browser.
  #---to check any dialog name is invoking the dialogs for reactive type of message---#
    You need to test dialog name given in the botname.py file ( for example check with 'introduction' ,'work-start' and 'work-end' for taskbot.py)
