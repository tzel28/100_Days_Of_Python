"""We are going to build a Rock, Paper and Scissors game"""
#we're going to use the random module  
import random 

#we are going to create the ASCII art to be used in our applictions 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Making the welcoming statement 
print("Welcome to the R.P.S game which stands for Rock, Papaer, and Scissors!\nLet's try your luck")
print('')

#make the variable where we are going to store and later call in the images 
images = [rock, paper, scissors]

#ask for the user input and store it in variable and convert it to an integer 
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(images[user_choice]) 

#use a function from the random module to be able to have the computer randomly generate between the number 0-2 like how we have our users do. 
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(images[computer_choice])

#we're going to use an if-else satement 
if user_choice >= 3 or user_choice < 0: # we make this statement if numbers are not within the allowed range 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")




