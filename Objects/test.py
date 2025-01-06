from Objects.Obj6 import animal,Wolf,Sheep,Parrot,Snake,zoo_list

from dataclasses import dataclass,field
from random import randint
from typing import List

@dataclass
class Cage():
    cage_id : int = field(default_factory=lambda : randint(100,1000))
    cage_detail : List[str] = field(default_factory=list) 

    cage_id = zoo_list[1], 
    def add_animals(self,*args):
        for arg in args:
            self.cage_detail.append(arg)

    def __repr__(self):
        output = f"\n \t Cage {self.cage_id} houses:\n { self.cage_detail}"

        return output

c1 = Cage(zoo_list[1],zoo_list[2])

if __name__ == "__main__":
    print(c1)


