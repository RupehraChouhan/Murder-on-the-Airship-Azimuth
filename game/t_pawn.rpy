label t_pawn:
    scene bg whiteImage
    show pawn
    with fade 
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_PAWN]
        
        # NPC speaks
        character.speakADV("What do you want to say to me?")
        Game.inputADV("Say something:")
        Game.checkQuit()
        character.speakADV("You said \"[Game.input]\"")
        Game.jump(character.label)
