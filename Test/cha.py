class Characters:
    def __init__(self, hp=100, species="Human"):
        self.name = 'No name yet'
        self.hp = hp
        self.species = species


class Items:
    def __init__(self):
        self.placeholder = 0


class Monsters(Characters):

    pass


class Relics:   # The thing/items you can get after killing monsters
    def __init__(self):
        self.placeholder = 0


class Locations:
    def __init__(self):
        self.placeholder = 0


class Achievement:
    def __init__(self):
        self.placeholder = 0



