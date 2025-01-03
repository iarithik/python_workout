'''
Create classes for each of these types, 
such that we can print each of them and 
get a report on their color, species, and number of legs.
'''


from dataclasses import dataclass,field
@dataclass
class animal:
    color :str
    species: str = field(init=False)
    no_of_legs : int

    
    def __post_init__(self):
        self.species = self.__class__.__name__

    def __repr__(self):
        return f" the color of animal is {self.color} the species is {self.species} and it has {self.no_of_legs} legs"
    

class Sheep(animal):
    def __init__(self,color):
        super().__init__(color=color,no_of_legs=4)

class Wolf(animal):
    def __init__(self,color):
        super().__init__(color=color,no_of_legs=4)

class Snake(animal):
    def __init__(self,color):
        super().__init__(color=color,no_of_legs=0)

class Parrot(animal):
    def __init__(self,color):
        super().__init__(color=color,no_of_legs=2)

sheep = Sheep('white')
snake = Snake('green')
parrot = Parrot("white")
wolf = Wolf("grey")

zoo_list = [sheep,snake,parrot,wolf]

if __name__=="__main__":
    for s in zoo_list:
        print(s.species) 
        print(s.color) 
        print(s.no_of_legs)
        print(s)

