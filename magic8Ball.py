# Functions are mini programs inside programs
# A value being passed to a function call is an arguement
# Variables that have arguements assigned to them are parameters
# The value that a function call evaluates to is called the return value
# When using the def statment, you can specify  what the return value should be with a return statment

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    elif answerNumber == 5:
        return 'ASk again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

print(getAnswer(random.randint(1,9)))

# A function call can be used in an expression because the call evaluates to its return value