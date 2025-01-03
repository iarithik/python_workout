class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    
    def __str__(self):
        return self.flavor

def create_scoops():
    s1 = Scoop("chocolate")
    s2 = Scoop("vanilla")
    s3 = Scoop("persimmon")
    
    flavor_options = [s1, s2, s3]
    return flavor_options

if __name__ == "__main__":
    for scoop in create_scoops():
        print(scoop.flavor)
