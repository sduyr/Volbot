#----Author: Senjuti Dutta--
#---Run Echobot.py and whenever you type anything it will echo your last message  and reminder also works here whenever you type remind me to do ----[Task][Time] in seconds


import lib.volbot as vb
import lib.manager


# A chatbot that includes a single dialog that echoes your message

dialogs = {
    'echo': {
        'type': 'reactive',
        'default': True,
        'waterfall': [
            "You said: ",
        ],
    },


}

# echobot using volbot framework
echoBot = vb.VolBot(name='EchoBot', manager = lib.manager.DialogManager(dialogs = ''),dialogs = dialogs)


# start the bot server
echoBot.start()
