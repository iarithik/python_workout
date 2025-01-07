class circle():
    def __init__(self,sequence,number):
        self.sequence = sequence
        self.number = number
        self.index = 0
          
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= self.number:
                raise StopIteration
        rem = (self.index) % len(self.sequence)
        value = self.sequence[rem]
        self.index +=1
        return value
            
c = circle('abc', 5)
print(list(c)) 
        
