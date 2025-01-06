from collections.abc import Iterable

class MyEnnumerate():
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not isinstance(self.data, Iterable):
            print("Error received , given data is not iterable, kindly behave yourself")
            raise StopIteration
        
        if self.index >= len(self.data):
            print("bye bye")
            raise StopIteration
        
        value = self.data[self.index]
        self.index +=1
        return (value, self.index)
    

for value,index in MyEnnumerate("OhO"):
    print(f"the value is {value} and index is {index}")