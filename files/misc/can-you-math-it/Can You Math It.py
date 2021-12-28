from time import time, sleep
from random import randint, choice 

operations = ('+', '-', '*', '/') 

def givechal():
    # generate and solve equation, return both question and answer
    challenge = str(randint(1, 999)) + ' ' + choice(operations) + ' ' + str(randint(1, 999)) + ' ' + choice(operations) + ' ' + str(randint(1, 999))
    result = int(eval(challenge))
    return challenge, result

def main():
    # intro
    print('Can You Math It?')
    sleep(1) # add some arbitrary delay
    print('You have 5 seconds to answer each question')
    print('You have 100 questions to solve')
    print('Please give all answers to nearest integer')
    print('Good luck')
    sleep(1)
    for i in range(100): 
        challenge, result = givechal() # generate and store question and answer
        print('Solve ', challenge, ' :') # show the question
        start = time() # start a timer
        answer = input() # receive answer
        timetaken = time() - start # stop timer, calculate time taken
        if timetaken < 5 and answer == str(result): # if within time limit and correct answer
            print('Correct!')
            print('Next question')
        elif timetaken > 5: # if more than 5 secs taken
            print('Took longer than 5 seconds')
            exit()
        else: # answer wrong
            print('Wrong answer')
            exit()
    print('Congratulations! You CAN math it')
    print('The flag is IRS{FLAG_REDACTED}') # the flag goes here

if __name__ == '__main__':
    main() # run the program