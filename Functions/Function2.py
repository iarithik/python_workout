#that expects a single argument
	# 1. a string containing a simple math expression in prefix notation
	# 2. with an operator and two numbers. 

import operator
operation = '+ 2 3'

def calc( operation):
    operation_list = {'+': operator.add ,'-':operator.sub,'*': operator.mul,'/':operator.truediv,'%':operator.mod,'**':operator.pow }
    operation_string = operation.split()
    optr = operation_string[0]

    if optr in operation_list:
        op = operation_list.get(optr)
    result = op(int(operation_string[1]),int(operation_string[2]))
    return result
print(calc(operation))

