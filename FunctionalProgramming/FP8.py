import string
#my approach
'''
def gematria():
    sc_dict ={  chr(i): (i-96)
              for i in range(ord('a'),ord('z')+1)
    }
    print(sc_dict)

gematria()

'''

#author's approach
def gematria_dict():
    sc_dict ={ index:char
              for char, index in enumerate(string.ascii_lowercase , 1)
    }
    return sc_dict

