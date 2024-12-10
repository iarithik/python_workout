def join_numbers(num):
    op = [str(x) 
          for x in range(num)]
    return ','.join(op)

print(join_numbers(5))