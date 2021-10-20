92221#from math import e, tan
from PythagoreanTheorem import Pith
from SourcedBasic import calculator
import os

def Choice():
    print()
    print('Type 1 For a Basic Calculator')
    print('Type 2 to Calculate for Pythagoras')
    #print('And 3 If you want to Calculate for Tan')
    
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
    
    print()
    print('To Continue with MORE Math! 1')
    print('Alternitively, 2')

    B = float(input(''))

    if B == 1:
        Choice()

    elif B == 2:
        print('Goodbye Then! :)')

Choice()