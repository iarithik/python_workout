from Objects.Obj1 import Scoop, create_scoops
from Objects.Obj2 import Bowl

class BigBowl(Bowl):
    max_limit = 5
    def __init__(self):
        super().__init__()
            
    def __repr__(self):
        private_bowl =' '.join(scoop.flavor for scoop in self.bowl_scoop)if self.bowl_scoop else None
        return f'the bowl that your kid ordred is {private_bowl} and max scoops allowed are {self.max_limit}'
    
flavors = create_scoops()

b = BigBowl()
b.add_scoops(flavors[0],flavors[1])
b.add_scoops(flavors[2])
b.add_scoops(flavors[1],flavors[1])
b.add_scoops(flavors[2])

print(b)