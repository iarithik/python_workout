# why does this code not work? and how can you make it work regardless?? hmmmmmm????/?
from Objects.Obj6 import animal,Wolf,Sheep,Parrot,Snake,zoo_list

from random import randint
from typing import List

class Cage():
    def __init__(self):
        self.cage_id = randint(100,1000)
        self.cage_detail = []

    def add_animals(self,*args):
        for arg in args:
            self.cage_detail.append(arg)

    def __repr__(self):
        output = f"\n \t Cage {self.cage_id} houses:\n { self.cage_detail}"

        return output

c1 = Cage(zoo_list[1],zoo_list[2])

if __name__ == "__main__":
    print(c1)