init -998 python: # Other classes are given first priority to load, after Game class
    class NPC:
        
        #  Default color is white, default matching strings is an empty list
        def __init__(self, name, label, color="#ffffff", matches=[], alive=True):
            self.name = name # Name of NPC
            self.label = label # Label to jump to to begin conversation, None if no conversation
            self.color = color # Color of NPC name
            self.adv = Character(name, kind=adv, color=color)
            self.nvl = Character(name, kind=nvl, color=color)
            self.alive = alive # is the npc alive?
            
            self.matches = [] # List of strings that can be used to match this NPC
            if name: # Name only included if given one
                self.matches += [name.lower()]
            for m in matches:
                self.matches += [m.lower()]
        
        # Returns true if target matches any allowed string for this NPC
        def match(self, target):
            target = target.lower()
            for m in self.matches:
                if target == m:
                    return True
            return False
        
        # Says a line of dialogue from the given npc in ADV mode
        def speakADV(self, dialogue):
            renpy.say(self.adv, dialogue)
        
        # Says a line of dialogue from the given npc in NVL mode
        def speakNVL(self, dialogue):
            renpy.say(self.nvl, dialogue)
