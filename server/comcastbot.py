#   file:   comcastbot.py
#   description:
#       this file implements a Volbot specification for a bot designed for
#       Comcast tech support.
import lib.volbot as vb
import lib.manager


# The following is the dialog specification format that the VolBot framework should support.
# The keys, values, and types of this dictionary reflect the *correct* format. You should
# use this dialog structure as inspiration for your other VolBot use-cases in Part 3.

abc = {
    'introduction': {
        'type': 'reactive',
        'default': True,
        'waterfall': [
            "Hi, I’m TaskBot. I’ll message you later for task information.",
            "You said your name is: abc"
        ],
    },
    'help': {
        'type': 'reactive',
        'default': False,
        'waterfall': [
            "Hi! It sounds like you need help. What can I help you with?.",
            "Hmm. I don't think I know how to help with that. Please call our help line at 1-888-293-2910",
        ]
    },


}

# create a new VolBot
comcastBot = vb.VolBot(name='ComcastBot', manager = lib.manager.DialogManager(dialogs = ''),dialogs = abc)


# start the bot server
comcastBot.start()
