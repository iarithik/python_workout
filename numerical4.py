#global variables
hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15} 


def hex_output():
    hex_num = input("Please input your hex number").upper()
    check = validity(hex_num)
    if(check):
        int_num = hex_to_int(hex_num)
        print(f"Your hex number is {hex_num} its equivalent integer is {int_num} ")

def validity(string):
    n= len(string)
    error_val =""
    correct_val =""
    count_e = 0
    count_c = 0
    check = True
    for index,s in enumerate(string):
        if s not in hex_map.keys():
            error_val += s
            count_e +=1
        if s  in hex_map.keys():
            correct_val += s
            count_c +=1
    if count_e > 0:
        check= False
        if count_e ==1:
            noun_e ="is"
        else:
            noun_e="are"
        if count_c ==1:
            noun_c ="is"
        else:
            noun_c="are"
        print(f"Please enter correct hexadecimal number, your {count_c} correct characters {noun_c} {correct_val} and your {count_e} erreneous characters {noun_e} {error_val} ")
    return check

def hex_to_int(string):
    #always add ' '  to map characters from string
    n= len(string)
    sum = 0
    for index,s in enumerate(string):
        value = hex_map.get(s) 
        sum += value*(16**(n-1-index))
    return(sum)

hex_output()