"""In this python file we're going to building a type of 'blind auction' application where all bidders can submit thier bids, where no bidder knows any 
bid of the other person. The highest bidder gets to take the prize. """
import os # to be able use the clear function 
clear = lambda: os.system('cls')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {} #empty dicitonary store name and bid amount 
bidding_finished = False

def find_highest_bidder(bidding_record): #function to find the highest bid amount 
  highest_bid = 0 #keep track of the numbers entered 
  winner = "" 
  for bidder in bidding_record: #will loop through each of the keys 
    bid_amount = bidding_record[bidder] #we're storing the value from the keys into this variable 
    if bid_amount > highest_bid: #if the amount enter is higher than the one stored it will become the new highest bid
      highest_bid = bid_amount
      winner = bidder 
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished: #while variable is still false program will keep running until changed
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price #add to the dicitonary. Name = key, price = value
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True #this will stop the ilteration 
    find_highest_bidder(bids)
  elif should_continue == "yes": #this will clear the screen to be able to add more bids without seeing the pervious type info
    clear()
