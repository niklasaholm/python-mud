class Monster(object):
    
    damage = 1

    def __init__(self, name):
        self.name = name

    def attack(self):
        return self.damage



class Dragon(Monster):

    def __init__(self, damage, name):
        self.damage = damage
        self.name = name
 

