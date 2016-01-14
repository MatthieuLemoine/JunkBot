#####
## Junk Bot IA Answer process
#####
import os
from datetime import datetime
from utils import *

junkIa = '\rSorry Sir. The current version of my IA did not allow me to understand your answer.\nRemember to update me soon.'

def greetings(userInput):
    if ('fine' in userInput) | ('good' in userInput) | ('great' in userInput):
        if 'not' in userInput:
            utils.jprint('\rDo not worry Sir.\nI am here now.')
        else:
            utils.jprint('\rI am glad to hear it Sir.')
    else:
        utils.jprint(junkIa)

def command(userInput):
    if 'reboot' in userInput:
        utils.jprint('Allright Sir. I reboot the computer for you')
        utils.jsysprint('Rebooting computer...')
        os.system('sudo shutdown -r now')
    elif 'shutdown' in userInput:
        utils.jprint('Allright Sir. I shutdown the computer for you')
        utils.jsysprint('Computer shutdown...')
        os.system('sudo shutdown -h now')
    elif ('stop' in userInput) | ('goodbye' in userInput) | ('sleep' in userInput):
        currentHour = datetime.now().hour
        greeting = 'Have a nice day.'
        if currentHour >= 21:
            greeting = 'Good night.'
        elif currentHour >= 17:
            greeting = 'Have a nice evening.'
        utils.jprint('Goodbye Sir. '+greeting)
        exit(0)
    else:
        utils.jprint(junkIa)
