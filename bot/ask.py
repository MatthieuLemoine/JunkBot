#####
## Junk Bot IA Ask process
#####
from datetime import datetime
import conf.conf as conf
import utils.utils as utils
import bot.answer as answer

def greetings():
    # TODO check meteo
    currentHour = datetime.now().hour
    greeting = 'Good morning'
    if currentHour >= 17:
        greeting = 'Good evening'
    elif currentHour > 12:
        greeting = 'Good afternoon'
    utils.jprint(greeting+' '+conf.adminName+'.\nHow are you today ?')

def askCommand():
    utils.jprint('How can I help you ?')

def askLoop():
    askCommand()
    userInput = utils.jinput()
    return answer.command(userInput)
