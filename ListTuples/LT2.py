from collections.abc import Sequence
from numbers import Number
def mysum(*inp):
    output ='' 
    for element in inp:
        if type(element) == str:
            output += element
        elif isinstance(element, Sequence):
            output += ''.join(map(str, element))  
        elif isinstance(element,Number):
            output = sum(inp)
        else:
            print(f"{element} is of type {type(element)} ,Please be serious and enter correct things, whyyyy??")
    print(output)

if __name__ == "__main__":
    mysum('abc','def')
    mysum([1,2,3], [4,5,6])
    mysum(1,2,3)
    mysum(1.2,5.000,3.234)
    mysum({1,2,3,4,56,9})
    mysum(('sssss','iiiiiisssssssss'))

#.join() is applicable to both list and tuple