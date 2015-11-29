label t_bishop:
    
    stop music fadeout 2
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_BISHOP]
        
        # NPC speaks
        Game.prevNarrate = "What do you want me to say"
        Game.jump(character.label + "_loop")
        
label t_bishop_loop:
    python:
        # define line and give options
        # in this case, the line is whatever the character last said.
        line = Game.prevNarrate
        choices = ["Tell me about yourself.", "What is your connection to the victim?", "Describe what you saw this evening", "Ask about a discovery", "Ask about another suspect", "Leave"]
        
        # say line and give options
        #character.speakADV(line)
        character.inputADV(line, choices)
        Game.checkQuit()
        
        try:
            index = int(Game.input) - 1
            if index == 0:
                Game.jump(character.label + "_you")
            elif index == 1:
                Game.jump(character.label + "_vic")
            elif index == 2:
                Game.jump(character.label + "_saw")
            elif index == 3:
                Game.jump(character.label + "_found")
            elif index == 4:
                Game.jump(character.label + "_other")
            elif index == 5:
                Game.jump("start")
            else:
                raise ValueError("wrong choice")

        except ValueError:
            character.speakADV("I don't know what you mean")
        
        Game.jump(character.label + "_loop")
        
label t_bishop_you:
    python:
        Game.jump(character.label + "_loop")
label t_bishop_vic:
    python:
        Game.jump(character.label + "_loop")
label t_bishop_saw:
    python:
        Game.jump(character.label + "_loop")
label t_bishop_found:
    python:
        line = "Ask about what?"
        choices = [ ]
        
        for clueName,found in Game.cluesFound.items():
            if found:
                choices.append(clueName)
        choices.append("Ask something else")
        
        Game.inputADV(line, choices, True)
        
        index = int(Game.input) - 1
        clueName = choices[index]
        if clueName == Game.BATHS_WOUND:
            pass
        elif clueName == Game.BATHS_TIME_OF_DEATH:
            pass
        elif clueName == Game.GALLEY_PIPE:
            pass
        elif clueName == Game.CABINS_EMPTY:
            pass
        elif clueName == Game.DINING_SPECTACLES:
            pass
        elif clueName == Game.LOUNGE_CONTRACTS:
            pass
        elif clueName == Game.GALLEY_BOOK:
            pass
        elif clueName == Game.CARGO_RECORD:
            pass
        #elif clueName == TODO add rook body
            pass
        else:
            character.speakADV("I don't know what you're talking about.")
        Game.jump(character.label + "_loop")
label t_bishop_other:
    python:
        Game.jump(character.label + "_loop")
label t_bishop_bishop:
    python:
        Game.jump(character.label + "_loop")
label t_bishop_knight:
    python:
        Game.jump(character.label + "_loop")
label t_bishop_pawn:
    python:
        Game.jump(character.label + "_loop")
label t_bishop_queen:
    python:
        Game.jump(character.label + "_loop")
