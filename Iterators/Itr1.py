class MyEnnumerate():
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try :
            if self.index >= len(self.data):
                raise StopIteration
            value = self.data[self.index]
            self.index +=1
            return (value, self.index)
        except Exception as e:
            print(f" error: {e}")
            raise ValueError

for value,index in MyEnnumerate(1):
    print(f"the value is {value} and index is {index}")