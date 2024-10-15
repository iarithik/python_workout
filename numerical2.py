def mysum(*numbers):
    output = 0
    for number in numbers:
        output +=number
    print(f'sum of numbers is {output}')
    return output

print(mysum(5,6,9))