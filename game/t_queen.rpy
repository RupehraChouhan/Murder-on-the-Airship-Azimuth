label t_queen:
    scene bg whiteImage
    show queen
    with fade 
    stop music fadeout 2
    
     
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_QUEEN]
        
        # NPC speaks
        line = "What do you want me to say"
        choices = ["Hello", "Hello", "I don't know why you say goodbye", "I say hello"]
        
        character.speakADV(line)
        character.inputADV(line, choices)
        Game.checkQuit()
        
        try:
            index = int(Game.input) - 1
            choice = choices[index]
            character.speakADV(choice)
        except:
            character.speakADV("I don't know what you mean")
        
        Game.jump(character.label)
