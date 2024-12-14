def supervolic(word):
    set_word = set(word.lower())
    vowels = {'a','e','i','o','u'}
    if vowels < set_word:
        return True
    else:
        return False

def get_sv(filename):
    #return set
    with open( filename,'r') as f:
        op = { word.strip()
            for word in f if supervolic(word)
        }

    return len(op)

print(get_sv('D:/Hottie/Files/words.txt'))