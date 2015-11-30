label finale:
    python:
        queen = Game.npcs[Game.NPC_QUEEN]
        knight = Game.npcs[Game.NPC_KNIGHT]
        rook = Game.npcs[Game.NPC_ROOK]
        pawn = Game.npcs[Game.NPC_PAWN]
        bishop = Game.npcs[Game.NPC_BISHOP]
        
        potentials = {Game.NPC_QUEEN:True, Game.NPC_KNIGHT:True, Game.NPC_BISHOP:True, Game.NPC_ROOK:True, Game.NPC_PAWN:True}
        
        # prelude, characters talking, you talking
        # establish the facts
        # weapon
        # weapon location
        # nobody was together at the time of the murder
        if Game.cluesFound[Game.BATHS_TIME_OF_DEATH]:
            # state time of death
            pass
        else:
            pass
            
        Game.jump("finale_main")

label finale_main:
    python:
        # address each in turn and evaluate motives and opportunity
        line = "Who do would you like to talk about?"
        choices = []
        for i in range(0, len(Game.npcs)):
            if i in potentials and potentials[i]:
                choices.append(Game.npcs[i])
    
        Game.inputADV(line, choices)
        index = int(Game.input) - 1
        choice = choices[index]
        Game.jump("finale_address_", choice.name.lower())
        
label finale_address_queen:
    python:
        # address QUEEN
        # mention - relationship, large inheritance, whereabouts, what people said
        # reject, keep, accuse
        if Game.state[Game.CONV_QUEEN_WHAT]:
            pass
        if Game.state[Game.CONV_BISHOP_WHAT_PRESS]:
            pass
        if Game.state[Game.CONV_KNIGHT_WHAT] or Game.state[Game.CONV_CAPTAIN_WHAT]:
            pass
            
        line = "But is she guilty?"
        choices = ["Guilty", "Innocent", "Potential"]
        Game.narrateADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            # guilty
            pass
        elif index == 1:
            potentials[Game.NPC_QUEEN] = False
            pass
        elif index == 2:
            pass
        Game.jump("finale_main")
        
        
label finale_address_rook:
    python:
        # address ROOK
        pass
        
label finale_address_bishop:

label finale_address_knight:

label finale_address_pawn:

label finale_accuse_queen:
    python:
        queen.speakADV("Me? What possible reason could I have?")
        # a few choices
        
label finale_accuse_knight:

label finale_accuse_rook:

label finale_accuse_bishop:

label finale_accuse_pawn: