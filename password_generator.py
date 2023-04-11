import random
import string

#create a function to generate password with three parameters to meet
def gen_pw(min_length, numbers=True, special_characters =True):
    # pass
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # print(letters, digits, special) 
        # output:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    
    characters = letters
    # if numbers, add those to letters
    if numbers:
        characters += digits
    # if specials, add those to letters
    if special_characters:
        characters += special

# generate a loop until some criteria's are met and store it to a password, pwd
    pwd =""
    meets_criteria = False # once meets critiera, these will pass true. but initially, set to false as default
    has_number= False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number #if has number it sets the meets_criteria to that numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special #to continue on from previous meets_criteria

    return pwd

# run customize fxn based on user input
    # based on user input, these variables will return interger, boolean, boolean for function to pass as paremeters
min_length = int(input("Enter the minimum length you want for your passowrd: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y" #returns lowercase if input was capital and reads it as "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() =="y"
pwd = gen_pw(min_length, has_number, has_special)
print("The generated password is:", pwd) 

# use cmd to run: python password_generator.py 

# -----sample output--------
# $ python password_generator.py 
# Enter the minimum length you want for your passowrd: 20
# Do you want to have numbers (y/n)? y
# Do you want to have special characters (y/n)? y
# The generated password is: xs|BZRDp@P{VL~~Bb~BF['J*g@LLE3






#call the fxn to test it out
# gen_pw(10); 
# gen_pw(10, False, True);

# pwd = gen_pw(10)
# print(pwd) 
#print and run or use cmd to run: python password_generator.py 