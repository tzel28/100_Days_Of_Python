"""In this python file we are creating an encryption and decryption appliction where a user can type in any message and enter the shift amount wanted to encrypted the message
Programmer: Thomas """

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z',]

direction = input("Type 'encode' to encrypt your a message, type 'decode' "
               "to decrypt a message:\n ") 

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number you would like:\n"))


#going to create the fucntion named 'encrypt' that will take the user input text and shift input
def encrypt():
    new_msg="" #we going to create an empty string for the new encrypt message

    for i in text: #using a for statment to loop through the text so each character gets shifted 
        if i.isalpha(): #.isalpha is a string method that checks if all the char in 'text' are letters of the alphabet 
            a = ord(i) + shift #ord() coverts a char to an integer adding the shift number the user selected 
            new_msg +=chr(a) #chr() converts the numbering of shift letters back into characters and puts them in empty string we created 
        else:
            new_msg += i
    print(f"Your encypted message is: {new_msg}")

def decrypt(encrypted_msg, shift_amount): #this will be the decrypt function. It will shift each letter of the encrypted message backwards from the alphabet by the shift amount.
    msg_dcrypt = '' #initialize an empty string to store the decrypted message

    for i in encrypted_msg: #using a for loop statment to loop through each letter in the encrypted message
        position = alphabet.index(i) #getting ahold of the position of each letter that is in the alphabet
        new_position= position - shift_amount #getting the NEW position by taking the current position and subtracting it by the shift amount 
        msg_dcrypt += alphabet[new_position] #once we got the new position of the letters we can add it to empty string variable  
    print(f"The decoded message reads: {msg_dcrypt}")


"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"



#using an if statment to allow the user to make his selection 
if direction == "encode":
    encrypt()
elif direction == "decode":
    decrypt(encrypted_msg=text, shift_amount=shift)
else:
    print("Not one of the selections. Try again")

