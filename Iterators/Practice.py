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

