import random


class Creature:
    # using magic method to initialize the Creature class with name and level
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print("The wizard {} attacks {}!"
              .format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level
        # creature_roll = random.randint(1,12) * creature.level
        creature_roll = self.get_defensive_roll()

        print("you roll {}".format(my_roll))
        print("{} rolls a {}".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("You have triumphed over a {}".format(creature.name))
            return True
        else:
            print("You have been defeated")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 3


class Predator(Creature):
    pass


class Dragon(Creature):
    def __init__(self, name, level, scales, breathes_fire):
        super().__init__(name, level)
        self.breates_fire = breathes_fire
        self.scales = scales

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breates_fire else 1
        scale_modifier = self.scales / 10

        return base_roll * fire_modifier * scale_modifier


class Creature:
    # using magic method to initialize the Creature class with name and level
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature: {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level
