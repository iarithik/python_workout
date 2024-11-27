#imports
import os
import csv

def process_line(current_line):
    words = current_line.split(':')
    op_list = [words[0],words[2]]
    return op_list


def passwd_to_csv(ip_file,op_file):
    try :
        with open(ip_file,'r') as ip:
            with open(op_file,'w',newline='') as op:
                o = csv.writer(op, delimiter='\t')

                for current_line in ip:
                    if current_line.startswith('#') or current_line.count(':') < 2:
                        continue
                    else:
                        o.writerow(process_line(current_line))

    except FileNotFoundError:
        print(f"Given input file {ip_file} doesn't exist. Please enter correct file")
    except Exception as e:
        print(f"Please take a look at the error {e}")

    return op_file

if __name__ =='__main__':
    ip_file = 'D:/Hottie/Files/passwd.txt'
    op_file = 'D:/Hottie/Files/processed_passwd.csv'

    op = passwd_to_csv(ip_file,op_file)

