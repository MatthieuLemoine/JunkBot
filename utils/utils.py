#####
## Junk Bot utils fonctions
#####
import time
import sys
import os
import conf.conf as conf

# Junk print
def jprint(output):
    jdivider()
    print(conf.botName + " : ")
    for c in output:
        time.sleep(0.1)
        sys.stdout.write(c);
        sys.stdout.flush()
    print('')
    jdivider()

# System print
def jsysprint(output):
    for c in output:
        time.sleep(0.1)
        sys.stdout.write(c);
        sys.stdout.flush()
    print('')

# Admin input
def jinput():
    jdivider()
    print(conf.adminName + " : ")
    userInput = sys.stdin.readline().lower()
    jdivider()
    return normalizeInput(userInput)

def jldivider():
    time.sleep(0.1)
    print("******************************")
    time.sleep(0.1)
    print("******************************")
    time.sleep(0.1)

def jdivider():
    time.sleep(0.1)
    print("******************************")
    time.sleep(0.1)

def jmode(output):
    jldivider()
    print(output)
    jldivider()

def jprogressbar(step):
    for i in range(101):
        time.sleep(0.05)
        if (i % step) == 0:
            progress = '#' * (i//step) + ' '*(100//step-(i//step))
        sys.stdout.write("\r[%s]%d%%" % (progress,i))
        sys.stdout.flush()
    print('')

# Meaningless words
stop_list = ['a','an','the','this','these','those','which','that','for','of','to','in']

def normalizeInput(userInput):
    return ' '.join([word for word in userInput.lower().split() if word not in stop_list])
