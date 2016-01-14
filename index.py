#!/usr/bin/env python3

#####
## Junk Bot
## A junk but awesome bot
#####

import time
import sys
from utils import *
from conf import *
import bot.answer as answer
import bot.ask as ask

utils.jmode(conf.botName + " Bot " + conf.botVersion)

# Boot process
utils.jsysprint("Initializing...")
utils.jprogressbar(2)
utils.jmode(conf.botName + " boot sequence completed")

# Greetings
ask.greetings()
userInput = utils.jinput()
answer.greetings(userInput)

# Commands
utils.jmode("Command mode enabled")
ask.command()
userInput = utils.jinput()
answer.command(userInput)
