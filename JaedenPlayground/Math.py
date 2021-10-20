
from PithagoreanTheorem import Pith
from SourcedBasic import calculator


def Choice():
    print('Or Type 1 For a Basic Calculator')
    print('Type 2 to Calculate for Pithagoras')
    #print('And 3 If you want to Calculate for Tan')
    #TODO: I sugest you use better names for variables because it is hard to under stand what is happening
    A = float(input(''))

    if A == 2:
        Pith()

    elif A == 1:
        calculator()

    #elif A == 3:
        #C = float(input('Solve for angle:1, Opp:2 or Adj:3 '))
        
        #if C == 1:
            #
        #elif C == 2:

            #
        #elif C == 3:
    
    print('To Continue with MORE Math! 1')
    print('Alternitively, 2')
#TODO: I sugest you use better names for variables because it is hard to under stand what is happening
    B = float(input(''))

    if B == 1:
        Choice()

    elif B == 2:
        print('Goodbye Then! :)')

Choice()