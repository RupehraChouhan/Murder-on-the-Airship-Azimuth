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
    # address each in turn and evaluate motives and opportunity
        
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
            # innocent
            pass
        elif index == 2:
            # potential
            pass
        Game.jump("finale_main")
        
        
label finale_address_rook:
    python:
        # address ROOK
        pass
        
label finale_address_bishop: