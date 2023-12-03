"""We are going to build a tip calculator in this python file. We are going to implement f-strings, data type conversions"""
import pyfiglet#we're going to pyfiglet to give the welcoming message more emphasis

#Start with the welcoming message to the users
message = pyfiglet.figlet_format("Welcome to the tip calculator") #figlet_format method convert ASCII text into ASCII art fonts.

print(message)

bill = float(input("What was the total bill? $")) #we are going to take the first user input and store it in a variable called 'bill' and automatically convert it to a float 

tip = int(input("What percentage tip would you like to give? 10, 12, or 15: ")) #this will be the second user input taken and we're going to store it in variable called 'tip' and automatically convert it to a integer


percent = tip /100 #we are converting the tip into a percentage


tip2 = bill * percent #we are going to take the percentage and mulitply it with the orgianl bill.  This will give us what tip percentage for the bill is


add_tip = tip2 + bill #we take that tip percentage from tip2 and add it to the orginal bill and it will give us our total


split = int(input("How many poeple are going to be sliting the bill? ")) #this will be the final user input taken and we're going to store it in a variable called 'split' and convert it to an integer automatically 

total_bill = add_tip / split #we're taking the orginal bill and added_tip and dividing it by the number of people that are going to split it 

final=round(total_bill, 2) #we're going to print the final total bill and round it two places by using the round function by telling ot the number of places by ' ,2 '

print(f"Each person should pay: ${final}")#we're going to use f strings in the final print statment 