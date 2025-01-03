from Objects.Obj1 import Scoop, create_scoops

class Bowl:
    max_limit =3
    shared_list = []
    def __init__(self):
        self.bowl_scoop =[]

    def add_scoops(self,*args):
        for i in args:
            if len(self.bowl_scoop)< self.max_limit:
                self.bowl_scoop.append(i)
          
    def __repr__(self):
        private_bowl =' '.join(scoop.flavor for scoop in self.bowl_scoop)if self.bowl_scoop else None
        shared_bowl = ' '.join(scoop.flavor for scoop in self.shared_list)if self.shared_list else None
        return f'the bowl that your kid ordred is {private_bowl} and bowl allowed for everyone is {shared_bowl}'

if __name__== '__main__':
    flavors = create_scoops()

    b = Bowl()
    b.add_scoops(flavors[0],flavors[1])
    b.add_scoops(flavors[2])
    b.add_scoops(flavors[1],flavors[1])
    b.add_scoops(flavors[2])

    print(b)
