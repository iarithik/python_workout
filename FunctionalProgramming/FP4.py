
def translate_to_pig(word):
    vowels ="aeiou"
    output=""
    if (word[0].lower() in vowels):
            output = word+"way"
    else:
        output = word[1: ] + word[0].lower()+"ay"
    return output


def file_pl(filename):
    with open(filename,'r') as f:
        op_string = [ translate_to_pig(word)
                     for current_line in f
                      for word in current_line.split() ]
        return ' '.join(op_string)


print(file_pl('Files/random.txt'))

