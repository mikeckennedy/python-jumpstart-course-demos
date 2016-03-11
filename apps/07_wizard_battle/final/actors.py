class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )
