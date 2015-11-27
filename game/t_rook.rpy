label t_rook:
    stop music fadeout 2
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_ROOK]
        
        # NPC speaks
        character.speakADV("What do you want to say to me?")
        Game.inputADV("Say something:")
        Game.checkQuit()
        character.speakADV("You said \"[Game.input]\"")
        Game.jump(character.label)
