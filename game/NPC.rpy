init -998 python: # Other classes are given first priority to load, after Game class
    class NPC:
        # Static(ish) array of NPCs
        NUM = 6
        npc = [None] * NUM
        
        # NPC constants
        NARRATOR = -1
        KING = 0
        QUEEN = 1
        BISHOP = 2
        KNIGHT = 3
        ROOK = 4
        PAWN = 5
        
        #  Default color is white, default matching strings is an empty list
        def __init__(self, name, label, color="#ffffff", matches=[]):
            self.name = name
            self.label = label
            self.color = color
            self.adv = Character(name, kind=adv, color=color)
            self.nvl = Character(name, kind=nvl, color=color)
            
            self.matches = [] # List of strings that can be used to match this NPC
            if name:
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
        @staticmethod
        def speakADV(npc, dialogue):
            if npc == NPC.NARRATOR:
                renpy.say(Character(None, kind=adv), dialogue)
            else:
                renpy.say(NPC.npc[npc].adv, dialogue)
        
        # Says a line of dialogue from the given npc in NVL mode
        @staticmethod
        def speakNVL(npc, dialogue):
            if npc == NPC.NARRATOR:
                renpy.say(Character(None, kind=nvl), dialogue)
            else:
                renpy.say(NPC.npc[npc].nvl, dialogue)
