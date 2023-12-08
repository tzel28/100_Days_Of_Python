"""We're going to create a password generator that allows a user to choose how many letters, numbers, and symbols he would like """
"""In this python file we're going to use range function, loops, and list"""
import random


#create the lists we are going to incorperate
char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sym = ['!','@','#','$','%','^','&','*','(',")",'.',',','<','>','?','/','=','+']
num= ['1','2','3','4','5','6','7','8','9','0']


#Welcome message 
print("")
print("Welcome to the Password Master Generator! Let's make your accounts secure!")
print('')

#ask for the user input 
user = int(input("How many letters would you like to add to your password?\n "))
user_sym = int(input("How many symbols would you like to add to your password?\n "))
user_num = int(input("How many numbers would you like to add to your password?\n "))

password = [] #create an empty list so we can add to it 

#make a for loop to go through the list
for i in range(1, user + 1):
    password += random.choice(char) #randomly adds letter to the list 
    

for i in range(1, user + 1):
    password += random.choice(sym) #randomly adds symbols to the list 

for i in range (1, user + 1):
    password += random.choice(num) #randomly adds numbers to the list 

random.shuffle(password) #use the shuffle function to randomly shuffle the places of where the characters will be placed at 

#now we're going to the turn the list into a string 
_pass = '' #create an empty string so we can add to it 

for i in password: #run it through a for loop once more
    _pass += i

print(f'Your password is: {_pass}')
