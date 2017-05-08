#!/usr/bin/python3

import random

print('-------------------------------------')
print('        Guess the number App')
print('-------------------------------------')
print()

hidden_int = random.randint(0,1000)
guess_incorrect = True 

name = input('Please enter your name: ')

while guess_incorrect:
   
    user_guess = int(input('Guess a number between 0 and 1000: '))
   
    if user_guess == hidden_int:
        print("Correct!")
        guess_incorrect = False
    elif user_guess > hidden_int:
        print('Lower...')
    elif user_guess < hidden_int:
        print('Higher...')

print('Well done {}, the hidden number was {}.'.format(name, hidden_int))
print()
