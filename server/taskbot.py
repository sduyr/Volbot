#-- Author: Senjuti Dutta---
# Run taskbot.py Whenever you type any of the mentioned dialog name in chat then will invoke the waterfall.
#For proactive messages it will give you a reminder  to work-start and work-end at the scheduled time
#reminders gives you scheduled reminders  whenever you type whenever you type remind me to do ----[Task][Time] in seconds



import lib.volbot as vb
import lib.manager


# A chatbot for task management that includes three dialogs

dialogs = {
    'introduction': {
        'type': 'reactive',
        'default': True,
        'waterfall': [
            "Hi, I’m TaskBot. I’ll message you later for task information.",
        ],
    },
    'work-start': {
        'type': 'proactive',
        'default': False,
        'waterfall': [
            "What task do you want to work on today?",
            "What is the first step of working on this stask?",
        ]
    },

   'work-end': {
       'type': 'proactive',
       'default': False,
       'waterfall': [
           "What did you want to work on today?",
           "What do you want to work on tomorrow?",
       ]
   },


}

# create a new VolBot named taskbot
taskBot = vb.VolBot(name='TaskBot', manager = lib.manager.DialogManager(dialogs = ''),dialogs = dialogs)


# start the bot server
taskBot.start()
