class LoudIterator():
    def __init__(self,data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            print(f"Raised an exception out of bounds")
            raise StopIteration
        value = self.data[self.index]
        self.index +=1
        print(f'the item is {value} and index is  {self.index}') 
        return value

LO = LoudIterator('cat')

for one_item in LO:
    print(one_item)

def foo():
    yield 3
    yield 2
    yield 1

for one in foo():
    print(one)
