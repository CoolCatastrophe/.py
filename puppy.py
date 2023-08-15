class Puppy:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.hunger = 0
        self.tricks = []

    def add_trick(self, trick):
        if trick not in self.tricks and trick != "q":
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}")
    def perform_trick(self,perform):
        if perform in self.tricks:
            print(f"{self.name} can {perform}")
        else:
            print(f"{self.name} cannot do that trick: {perform}")

jamie = Puppy("Jamie", 2, "Dalmatian")

print(jamie.name)
print(jamie.age)
print(jamie.breed)
t=None
while True:
    if(t=="q"):
        break
    t = input("Type a Trick to Add(""q"" to quit): ")
    jamie.add_trick(t)

print(f"List of all tricks: {jamie.tricks}")
jamie.perform_trick("dance")