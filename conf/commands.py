#####
## Junk Bot Available commands
#####

# List of all commands availables with parameters
# TODO import commands from file i.e exec a file on command / command = module
# TODO automate command adding
commands = {
    'stop': {
        'botMessage' : 'Goodbye Sir.',
        'command' : 'exit(0)'
    },
    'reboot' : {
        'botMessage' : 'Allright Sir. I reboot the computer for you',
        'sysMessage' : 'Rebooting computer...',
        'command' : 'os.system(\'sudo shutdown -r now\')'
    },
    'shutdown' : {
        'botMessage' : 'Allright Sir. I shutdown the computer for you',
        'sysMessage' : 'Computer shutdown...',
        'command' : 'os.system(\'sudo shutdown -h now\')'
    }
}

# Define trigger words for each command
# TODO automate triggers adding
triggers = {
    'stop' : 'stop',
    'goodbye' : 'stop',
    'sleep' : 'stop',
    'reboot' : 'reboot',
    'shutdown' : 'shutdown'
}
