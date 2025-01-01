
from Strings import string1 as s

def file_pl(filename):
    with open(filename,'r') as f:
        op_string = [ s.translate_to_pig(word)
                     for current_line in f
                      for word in current_line.split() ]
        return ' '.join(op_string)


print(file_pl('Files/random.txt'))

