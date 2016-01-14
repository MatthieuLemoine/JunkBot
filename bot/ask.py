#####
## JunkOS Bot IA Ask process
#####
from datetime import datetime
from conf import *
from utils import *

def greetings():
    # TODO check meteo
    currentHour = datetime.now().hour
    greeting = 'Good morning'
    if currentHour >= 17:
        greeting = 'Good evening'
    elif currentHour > 12:
        greeting = 'Good afternoon'
    utils.jprint(greeting+' '+conf.adminName+'.\nHow are you today ?')

def command():
    utils.jprint('How can I help you today ?')
