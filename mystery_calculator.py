##
# mystery_calculator.py
# 14/04/2021
# Rhiannon MacCreadie
# Creates a mystery calculator program
import time
# To create suspense


def group_lists():
    """
    populates a list with 6 lists
    Returns list
    """
    # Create list
    mystery_calculator = []
    # Populate with other lists
    mystery_calculator.append(list_1())
    mystery_calculator.append(list_2())
    mystery_calculator.append(list_3())
    mystery_calculator.append(list_4())
    mystery_calculator.append(list_5())
    mystery_calculator.append(list_6())
        

    return mystery_calculator


def list_1():
    """
    Fills a list starting from 1 to 63 going up in 2
    Returns list
    """
    # Create list to put values into
    list_1 = []
    # Add values automatically
    for i in range(1, 64, 2):
            list_1.append(i)
    return list_1
            

def list_2():
    """
    Populates a list with digits from 2 to 63
    Adds alternating values between each number
    evens = 2i + 2
    odds = 2i + 1
    Returns list
    """
    # Create a list to populate 
    list_2 = []
    
    for i in range(32):
        # Reset number value
        number = 0
        if i % 2 == 0:
            number = (i * 2) + 2
            list_2.append(number)
        else:
            number = (i * 2) + 1
            list_2.append(number)
       
    return list_2
    

def list_3():
    """
    Populates a list with digits from 4 to 63
    Uses a different equation at every 4th digit(starting with 4)
    four = 2i + 4
    equation = i + 4n (where n goes up by one everytime it is called)
    Returns list
    """
    # Create a list to populate 
    list_3 = []
    # Defining counter that acts as i in equation
    counter = 0
    
    for i in range(32):
        # Reset number value
        number = 0
        if i % 4 == 0:
            number = (2 * i) + 4
            counter += 1
            list_3.append(number)
        else:
            number = i + (4 * counter)
            list_3.append(number)
       
    return list_3


def list_4():
    """
    Populates a list with digits from 8 to 63
    Changes equation every 8th digit
    equation = i + (counter * 8)
    (where at ever 8th digit add one to counter)
    Returns list
    """
    # Create a list to populate 
    list_4 = []
    # Defining counter that acts as i in equation
    counter = 0
    
    for i in range(32):
        # Reset number value
        number = 0
        if i % 8 == 0:
            counter += 1
            
        number = i + (counter * 8)
        list_4.append(number)
        
       
    return list_4


def list_5():
    """
    Populates a list with digits from 16 to 63
    Changes equation at the 16th digit
    first equation = i + 16
    second equation = i + 32
    Returns list
    """
    # Create a list to populate 
    list_5 = []
    
    
    for i in range(32):
        # Reset number value
        number = 0
        if i < 16:
            number = i + 16
            list_5.append(number)
        else:
            number = i + 32
            list_5.append(number)
       
    return list_5

    
def list_6():
    """
    Populates a list with digits from 32 to 63 in order
    """
    # Create a list to populate 
    list_6 = []
    # Create a list to populate 
    list_6 = []
    
    for i in range(32, 64):
        list_6.append(i)
        
    return list_6


def pretty_print(mystery_calculator):
    """
    Runs through each list, pretty prints it,
    adds value to number
    returns number
    """
    ANSWERS = [["yes","ya","yep","yup","y","yah", "yeh"],
               [ "n", "nope", "nah", "no", "nah", "neh"]]
    # Create variable to hold predicted number
    number = 0
    answer = " "

    # for list in list
    for i in range(len(mystery_calculator)):
        answer = " "
        print()
        # asks for answer until in ANSWERS
        while answer not in ANSWERS[0] and answer not in ANSWERS[1]:   
            # for number in list
            for j in range(len(mystery_calculator[i])):
                # if first one add a blank line
                if j % 6 == 0:
                    print()
                # pretty prints list
                print(mystery_calculator[i][j], end = " ")
            # ads space

            print("\nPlease answer a clear Yes or No.")
            answer = input("\nIs your number in this list? ")
            answer.lower()


        # Adding value to prediction
        if answer in ANSWERS[0]:
            number += mystery_calculator[i][0]
        else:
            continue
    return number
    
  
def game(mystery_calculator):
    """
    A series of print statements.
    Asks user to think of a number.
    Prints predicted number
    """
    
    print("Think of a number between 1 and 63")
    
    # Shows dots to show the prgram is waiting every second for 3 seconds
    for i in range(3):
        print(".")
        time.sleep(1)

    #Tells the user what the program will do
    print("Ok" +
          " I will now predct your number using this simple yes or no system")
    time.sleep(1)
      
    number = pretty_print(mystery_calculator)
    for i in range(3):
        print(".")
        time.sleep(1)
    print("\n{} was your number.".format(number))
    

# Main Program
while __name__ == "__main__":
    mystery_calculator = group_lists()
    game(mystery_calculator)
