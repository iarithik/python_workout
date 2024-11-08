def mysum(*numbers):
    output = 0
    for number in numbers:
        output +=number
    print(f'sum of numbers is {output}')
    return output

if __name__ == "__main__":
    print(mysum(5,6,9))