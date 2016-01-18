#####
## Junk Bot IA Analyse user input process
#####
from conf.commands import commands
from conf.commands import triggers
import utils.utils as utils

mean_words = ['dumb','fuck','shit','damn','shut up']
good_words = ['good','fine','great','well']
change_words = ['change','modify','alter']
show_words = ['show','display','see']

# Meaningless words
stop_list = ['a','an','the','this','these','those','which','that','for','of','to','in']

def isMean(userInput):
    return any(s in userInput.lower() for s in mean_words)

def isGood(userInput):
    return any(s in userInput.lower() for s in good_words)

def isChange(userInput):
    return any(s in userInput.lower() for s in change_words)

def isShow(userInput):
    return any(s in userInput.lower() for s in show_words)

junkIa = '\rSorry Sir. The current version of my IA did not allow me to understand your answer.\nRemember to update me soon.'

# TODO exec a command file
def detectCommand(userInput):
    # Check if there is a command matching user input
    for trigger,commandKey in triggers.items():
        if trigger in userInput.lower():
            command = commands[commandKey]
            if 'botMessage' in command:
                utils.jprint(command['botMessage'])
            if 'sysMessage' in command:
                utils.jsysprint(command['sysMessage'])
            if 'command' in command:
                exec(command['command'])
            return True
    # If there is not
    utils.jprint(junkIa)
    return True

def normalizeInput(userInput):
    return ' '.join([word for word in userInput.lower().split() if word not in stoplist])
