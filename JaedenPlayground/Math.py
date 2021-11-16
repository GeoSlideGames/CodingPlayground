#TODO: find a way to add multiple anenswer to the if's
#TODO: make a function to check if a variable is a string or a number
# then use it to check if the user inputs anything but a number and tell them to give a nummber 
from PithagoreanTheorem import Pith
from Basic import calculator
from clearConsole import clearConsole


def Choice():
    print()
    print('Type 1 For a Basic Calculator')
    print('Type 2 to Calculate for Pithagoras')
    #print('And 3 If you want to Calculate for Tan')
    
    TypeOFQuestion = float(input(''))
    

    if TypeOFQuestion == 1:
        calculator()

    elif TypeOFQuestion == 2:
        Pith()
    
    #elif A == 3:
        #C = float(input('Solve for angle:1, Opp:2 or Adj:3 '))
        
        #if C == 1:
            #
        #elif C == 2:
            #
        #elif C == 3:
    print() #empty space to seprate
    print('To Continue with MORE Math! 1')
    print('Alternitively, 2')
    

    ContinuationChoice = float(input(''))

    if ContinuationChoice == 1:
        Choice()

    elif ContinuationChoice == 2:
        print() #empty space to seprate
        print('Goodbye Then! :)')
Choice()