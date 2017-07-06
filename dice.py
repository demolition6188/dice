#
#IMPORTS
#
import math
import random

#VARIABLES
rolling = True

#FUNCTIONS
def NumberError():
    print('Please enter a number.')

def TryAgain():
    print('Please try again.')

def Zero():
    print('Please enter a number... above Zero.')

def Dice(sides):
    try:
        return math.floor(random.random() * sides) + 1
    except VauleError:
        print('Please enter a number.')

#
#INTRO
#
print('This is a Dice Program.')

while rolling:
    print('I can roll multiple dice of multiple sizes.')

#
#HOW MANY DICE
#
    while True:
        print('How many dice are do you want to roll?')
        howMany = input()

        try:
            if int(howMany) <1:
                Zero()
                continue

            elif int(howMany) >1:
                if int(howMany) >10000:
                    print('Sorry, I would roll that many dice but it would take a long time.')
                    print('I don\'t think you have that much time, so pick a smaller number please.')
                    continue
                else:
                    howMany = int(howMany)
                    break

            else:
                TryAgain()
                continue

        except ValueError:
            NumberError()
            continue
#
#HOW MANY SIDES
#
    while True:
        print('How many sides on the dice?')
        sides = input()

        try:
            if int(sides) <1:
                Zero()
                continue

            elif int(sides) >1:
                sides = int(sides)
                break

            else:
                TryAgain()
                continue

        except ValueError:
            NumberError()
            continue
#
#ARE ANY DICE DIFFERENT?
#
    if howMany > 1:
        while True:
            print('Are any of the dice different? y/n <blank is n>')
            different = input()
            howManyDiff = 0

            try:
                if different == 'y':

                    while True:
                        print('How many are different?')
                        howManyDiff = input()

                        try:
                            if int(howManyDiff) < 1:
                                Zero()
                                continue

                            elif int(howManyDiff) > howMany:
                                print('There has to be less that are different than the total number of dice, silly!')
                                continue

                            elif int(howManyDiff) > 1:
                                howManyDiff = int(howManyDiff)
                                while True:
                                    print('How many sides are the different dice?')
                                    diffSides = input()
                                    try:
                                        if int(diffSides) < 1:
                                            Zero()
                                            continue

                                        elif int(diffSides) > 1:
                                            diffSides = int(diffSides)
                                            break

                                        else:
                                            TryAgain()
                                            continue


                                    except ValueError:
                                        NumberError()
                                        continue

                                break

                            else:
                                TryAgain()
                                continue

                        except ValueError:
                            NumberError()
                            continue

                    break

                elif different == '':
                    break

                elif different == 'n':
                    break
                else:
                    TryAgain()
                    continue

            except ValueError:
                NumberError()
                continue
#
#ROLLLLINNNGGGGGG
#
    print('Rolling')
    print('.' * 10)

#
#RESULTSSSS
#
    if howMany <= 1:
        dice = math.floor(random.random() * sides) + 1
        print('Your rolled a ' + str(dice))

    else :

        for i in range(1, (howMany +1), 1):

            if i > howManyDiff:
                dice = Dice(sides)
                print('Dice ' + str(i) + '(d'+ str(sides) + ')' + ' Rolled a ' + str(dice))

            elif i <= howManyDiff:
                diffDice = Dice(diffSides)
                print('Dice ' +str(i) + '(d'+str(diffSides)+')' + ' Rolled a ' + str(diffDice))

            else:
                print('beep boop boop beep')
                break
#
#ROLL AGAIN
#

    while True:
        print('Would you like to roll again? y/n <blank is y>')
        again = input()

        try:
            if again == 'y':
                break

            elif again == '':
                break

            elif again == 'n':
                rolling = False
                break

            else :
                TryAgain()
                continue
        except ValueError:
            NumberError()

print('Thanks for using dice.py created by demolition6188 <3')
