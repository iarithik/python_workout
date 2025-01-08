
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
'''
import time

start = time.perf_counter_ns()
# Your code to measure
end = time.perf_counter_ns()

print(f"Elapsed time: {end - start} seconds")
