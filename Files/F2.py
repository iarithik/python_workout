def passwd_to_dict(Filename):
    pwd_dict ={}
    with open(Filename,'r') as f:
        for current_line in f:
            comment = current_line.startswith('#')
            if comment:
                continue
            word = current_line.split(':')
            if len(word)>2 :
                pwd_dict.update({word[0]: word[2]})
            else:
                pwd_dict.update({word[0]: 'None'})
    return pwd_dict

if __name__ == '__main__':
    op = passwd_to_dict('Files/passwd.txt')
    print(op)
