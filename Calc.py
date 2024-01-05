"""We are going to construct calculator application. Where the user enters a number, picks out the operaton, enters the second number and than calculate  it.
The user is than able to conutine doing mathematical operations with the number that was calculated or start anew"""

from logo import logo
#addition 
def add(n1,n2):
    return n1 + n2

#Subtraction
def sub(n1,n2):
    return n1- n2

#Multiplication
def multiply(n1,n2):
    return n1 * n2

#Division
def divide(n1,n2):
    return n1 / n2

#dictonary operations is going to use as the means where we're going to call in our functions 
operations = {  
'+' : add,
'-': sub,
'*' : multiply,
'/': divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for keys in operations: #use a for loop to print out all the symbols from the dictonary 
        print(keys)
    should_continue = True #the flag to be used in our while loop

    while should_continue:
        operation_key = input("Pick an operations: ")
        num2 = float(input("What's the next number?: "))
        calculation = operations[operation_key] #we're going to use this function to be able to go through our dictonary using the operation key the user selects, which in turn selects the function to use
        answer = calculation(num1, num2) #we're going to use a varaible call answer to store our calculation that is done
        print(f"{num1 } {operation_key} { num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer #when it repeats back we make sure that num1 is equal to the answer from the pervious step
        else:
            should_continue = False #this will close out our application 
            calculator()
    
calculator()

    
    
    
    


