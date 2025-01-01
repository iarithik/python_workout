

def menu(**args):
    functions_dict = ' '.join(args)
    function_name = input(f'input function name you wish to call options are {functions_dict}')
    if function_name in args:
        return args[function_name]()
    else:
        print(" not valid ")


def func_a():
    return "A"
def func_b():
    return "B"

return_value = menu(a=func_a, b=func_b)
print(f'Result is {return_value}')