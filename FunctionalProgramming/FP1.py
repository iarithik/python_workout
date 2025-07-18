def join_numbers(num):
    op = [str(x) 
          for x in range(num)]
    return ','.join(op)

# below is the print function (added by Rithik)
print(join_numbers(5))
