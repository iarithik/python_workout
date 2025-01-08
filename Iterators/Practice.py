
'''
def __init__(self,sequence,number):
        self.sequence = sequence #abc
        self.number = number #5
        self.index = 0

def __next__(self):
        if self.index >= self.number:
                raise StopIteration
        rem = (self.number- self.index) % len(self.sequence)
        value = self.sequence[rem]
        self.index +=1
        return value

def time_counter():
    시간 = 5
    return (시간)

o = time_counter()
print(o)

import time
def elapsed_since(data):
        last_time = None 
        for item in data:
                current_time = time.perf_counter() 
                delta = current_time - (last_time
                or current_time) 
                last_time = time.perf_counter()
                yield (delta, item) 
for t in elapsed_since('abcd'):
        print(t)
        time.sleep(2)
'''