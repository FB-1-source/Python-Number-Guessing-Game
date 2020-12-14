#number guessing game

import random

print('Hello, what is your name?')
name = input()
      
print('Well, ' + name + ' pick a number 1-20')
secretNum = random.randint(1,20)

for guess in range (1,7):
    print('Take a guess')
    guess = int (input())

    if guess < secretNum:
      print ( 'Your guess is too low')

    elif guess > secretNum:
      print('Your guess is too high')

    else:
      break



if guess == secretNum:
      print('Congrats! you guessed ' + str(secretNum) + ' which was the correct number')

else:
      print( 'Nope the correct number was ' + str(secretNum) + '. Better luck next time.')
