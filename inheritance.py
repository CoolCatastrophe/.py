class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows!!")


class Cougar(Cat):
    def __init__(self, name, clan):
        super().__init__(name)
        self.clan = clan

    def purr(self):
        print(f"{self.name} purrs!!")


puma = Cougar("tina", "wild")
print(puma.clan)
puma.meow()
puma.purr()
