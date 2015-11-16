init -999 python: # classes are given first priority to load
    class NPC:
        def __init__(self, name, color):
            self.name = name
            self.npc = Character(name, kind=adv, color=color)