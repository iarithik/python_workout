import os

def read_lines(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory,filename)
        try:
            with open(file_path,'r',encoding='utf-8') as f:
                for line in f:
                    yield line
        except Exception as e:
            print(f' the error is {e}')
            pass

directory = 'D:/Hottie/Files/books'
op = read_lines(directory)
for line in op:
    print(line)