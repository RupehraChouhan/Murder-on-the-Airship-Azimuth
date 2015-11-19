init -998 python: # Other classes are given first priority to load, after Game class
    class NPC:
        # Static(ish) array of NPCs
        NUM = 6
        npc = [None] * NUM
        
        # NPC constants for array index, more can be added if we desire non-suspect NPCs
        NARRATOR = -1 # Narrator is not in the array
        KING = 0
        QUEEN = 1
        BISHOP = 2
        KNIGHT = 3
        ROOK = 4
        PAWN = 5
        
        #  Default color is white, default matching strings is an empty list
        def __init__(self, name, label, color="#ffffff", matches=[]):
            self.name = name # Name of NPC
            self.label = label # Label to jump to to begin conversation, None if no conversation
            self.color = color # Color of NPC name
            self.adv = Character(name, kind=adv, color=color)
            self.nvl = Character(name, kind=nvl, color=color)
            
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
