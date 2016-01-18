#####
## Junk Bot IA Answer process
#####
import os
import utils.utils as utils
import bot.analyse as analyser

junkIa = '\rSorry Sir. The current version of my IA did not allow me to understand your answer.\nRemember to update me soon.'

def greetings(userInput):
    if analyser.isGood(userInput):
        if 'not' in userInput:
            utils.jprint('\rDo not worry Sir.\nI am here now.')
        else:
            utils.jprint('\rI am glad to hear it Sir.')
    else:
        utils.jprint(junkIa)

def command(userInput):
    return analyser.detectCommand(userInput)
