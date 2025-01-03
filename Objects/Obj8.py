from Objects.Obj7 import Cage, c1, c2
from typing import List

class Zoo:
    def __init__(self):
        self.cage_list: List[Cage] = []
    
    def add_cages(self, *cages):
        self.cage_list.extend(cages)
    
    def animals_by_color(self, color):
        return [
            animal 
            for cage in self.cage_list 
            for animal in cage.cage_detail 
            if animal.color == color
        ]

    def animals_by_legs(self, legs):
        return [
            animal 
            for cage in self.cage_list 
            for animal in cage.cage_detail 
            if animal.no_of_legs == legs
        ]
    
    def number_of_legs(self):
        return sum(
            animal.no_of_legs 
            for cage in self.cage_list 
            for animal in cage.cage_detail
        )
    
    def __repr__(self):
        return ''.join(
            f"Cage ID {cage.cage_id} houses:\n" + 
            ''.join(f"\t{animal}\n" for animal in cage.cage_detail)
            for cage in self.cage_list
        )

# Usage
z = Zoo()
z.add_cages(c1, c2)
print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())