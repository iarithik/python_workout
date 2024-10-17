def strsort(string):
    og_string = list(string)
    n = len(og_string)
    if len(og_string) <2 :
        return og_string

#in each iteration the i'th biggest element will go to its order n
#so its okay to exclude and create subset which is 0 : n-i
    for i in range(n):
        for j in range(0,n-i-1):
            if og_string[j] > og_string[j+1]:
                og_string[j],og_string[j+1] = og_string[j+1],og_string[j]

    return(''.join(og_string))

if __name__ == "__main__":
    output = strsort("xdeeaee")
    print(output)









