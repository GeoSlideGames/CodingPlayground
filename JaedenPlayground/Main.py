from PithagoreanTheorem import Pith
from SourcedBasic import calculator


def Choice():
    print('Type 1 to Calculate for Pithagoras')
    print('Or Type 2 For a Basic Calculator')
    A = float(input(''))
    if A == 1:
        Pith()
    elif A == 2:
        calculator()

Choice()