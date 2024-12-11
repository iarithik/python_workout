
#approach 1
def sum_numbers_mf():
    ip = input("Please enter your expression")
    #filter the non digits from the ip
    op = ip.split()
    x = map(int, filter(str.isdigit, op))
    return sum(x)

print(sum_numbers_mf())

#approach 2
def sum_numbers():
    ip = input("Please enter your expression")
    op = ip.split()
    x = sum( int(i)
          for i in op if i.isdigit())
    return x
print(sum_numbers())

