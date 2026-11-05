class Player:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def take_damage(self,amount):
        self.health = self.health - amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def show_status(self):
        print(f"{self.name} HP: {self.health}")

class Wizard(Player):
    def __init__(self,name,health,mana):
        super().__init__(name,health)
        self.mana = mana

    def cast_spell(self,cost):
        if cost > self.mana:
            print(f"{self.name} has not enough mana")
        else:
            self.mana = self.mana - cost
            print(f"{self.name} casts a spell. Mana left: {self.mana}")

hemanth = Wizard("Hemanth", 100, 50)
hemanth.cast_spell(25)
hemanth.take_damage(40)
hemanth.show_status()
hemanth.cast_spell(40)
hemanth.take_damage(75)
hemanth.show_status()
print(hemanth.is_alive())
