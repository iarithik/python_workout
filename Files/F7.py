def reverse_file(ip_file,op_file):
    try :
        with open(ip_file,'r') as ip:
            with open(op_file,'w') as op:

                for current_line in ip:
                    op.write(f'{current_line.rstrip()[::-1]}\n')
                    

    except FileNotFoundError:
        print(f"Given input file {ip_file} doesn't exist. Please enter correct file")
    except Exception as e:
        print(f"Please take a look at the error {e}")

    return op_file

if __name__ =='__main__':
    ip_file = 'D:/Hottie/Files/ex24IP.txt'
    op_file = 'D:/Hottie/Files/ex24op.txt'

    op = reverse_file(ip_file,op_file)
    print(f' process content can be found at {op}')
