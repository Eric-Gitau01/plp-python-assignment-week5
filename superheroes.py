class Superhero:
    def __init__(self, name, secret_id):
        self.name = name
        self.secret_id = secret_id
    
    def introduce(self):
        print(f"I'm {self.name}! My secret identity is {self.secret_id}.")
    
    def use_power(self):
        print("Using generic superpower!")

class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} soars through the clouds! ✈️")

class StrongHero(Superhero):
    def use_power(self):
        print(f"{self.name} lifts 1000 tons! 💪")


hero1 = FlyingHero("Sky Guardian", "John Doe")
hero2 = StrongHero("Mighty Titan", "Jane Smith")


heroes = [hero1, hero2]
for hero in heroes:
    hero.introduce()
    hero.use_power()
    print("---")