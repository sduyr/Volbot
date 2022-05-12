
#----Author: Senjuti Dutta---
# Run reminderbot.py and get the reminders at scheduled times whenever you write remind me to do ----[Task][Time] in seconds




import lib.volbot as vb
import lib.manager


# A chatbot that allows to set reminders via message

dialogs = {
    'capture': {
        'type': 'reactive',
        'default': True,
        'waterfall': [
            "Hi, I’m ReminderBot! What would you like me to remind you about?",
            "Got it. I 'll remind you later."
        ],
    },

}

# create a new VolBot
reminerBot = vb.VolBot(name='ReminderBot', manager = lib.manager.DialogManager(dialogs = ''),dialogs = dialogs)


# start the bot server
reminderBot.start()
