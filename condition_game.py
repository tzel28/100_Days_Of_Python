"""This python will be game where users are able to choose what the next step will be"""
"""This program will incorparte conditaitonal statments, logical operators"""

import sys

#welcome statement 
print("Welcome to the Escape room\nYour goal is to get out of the room alive... joking just need to get out the room\nLets Start!")
print('')
door = input("You are coming up to two doors labled Left or Right. Which door will you choose? ").lower()

print('')
if door == 'left':
    fence = input("You chose to open the left door great!\n Now this  door leads to a table with a question."
                  "What is the biggest state in the U.S? ").lower()
    if fence == 'alaska':
        colors = input("Great answer! Final choice to get out the room.\n"
                       "What color gum drop will you eat? Green or Red ").lower()
        if colors == 'red':
            print("Oops wrong choice. Game Over! Bye Bye")
        elif colors =='green':
            print("Yay! You made it out. You win the game!")
    else:
        print("game over. BYe Bye")
else:
    print('game over. Bye Bye')

