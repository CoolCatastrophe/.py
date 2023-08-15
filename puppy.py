class Puppy:
    def __init__( self, name, age, breed ):
        self.name = name
        self.age = age
        self.breed = breed
        self.hunger = 0
        self.energy = 100
        self.happiness = 100
        self.health = 100
        self.alive = True
        self.sick = False
        self.sick_days = 0

jamie = Puppy( "Jamie", 2 )
print( jamie.name )
print( jamie.age )
print( jamie.breed )
print( jamie.hunger )
print( jamie.energy )