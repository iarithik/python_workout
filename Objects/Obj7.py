from Objects.Obj6 import animal,Wolf,Sheep,Parrot,Snake,zoo_list

from dataclasses import dataclass,field
from random import randint
from typing import List

@dataclass
class Cage():
    cage_id : int = field(default_factory=lambda : randint(100,1000))
    cage_detail : List[str] = field(default_factory=list) 
    

    def add_animals(self,*args):
        for arg in args:
            self.cage_detail.append(arg)

    def __repr__(self):
        output = f"\n \t Cage {self.cage_id} houses:\n"
        for animal in self.cage_detail:
            output += f"\t{animal}\n"
        return output

c1 = Cage()
c1.add_animals(zoo_list[1],zoo_list[2])

c2 = Cage()
c2.add_animals(zoo_list[0],zoo_list[3])

if __name__ == "__main__":
    print(c1)
    print(c2)