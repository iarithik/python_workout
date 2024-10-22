def mysum(*inp):
    output ='' 
    for element in inp:
        if type(element) == str:
            output += element
        elif type(element) == list:
            output += ''.join(map(str, element))  
        else:
            output = sum(inp)
    print(output)

mysum('abc','def')
mysum([1,2,3], [4,5,6])
mysum(1,2,3)