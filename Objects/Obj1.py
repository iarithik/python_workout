
class Scoop:
    flavor:str
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops():
    s1 = Scoop("chocolate")
    s2 = Scoop("vanilla")
    s3 = Scoop("persimmon")
        
    flavor_options = [s1, s2,s3]

    for i in flavor_options:
        print(i.flavor)
        print(id(i))

create_scoops()