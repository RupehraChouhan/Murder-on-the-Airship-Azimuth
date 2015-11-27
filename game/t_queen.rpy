label t_queen:
    scene bg whiteImage
    show queen
    with fade 
    stop music fadeout 2
    
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_QUEEN]
        
        # NPC speaks
        Game.prevNarrate = "What do you want me to say"
        Game.jump(character.label + "_loop")
        
label t_queen_loop:
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
        
label t_queen_you:
    python:
        Game.jump(character.label + "_loop")
label t_queen_vic:
    python:
        Game.jump(character.label + "_loop")
label t_queen_saw:
    python:
        Game.jump(character.label + "_loop")
label t_queen_found:
    python:
        line = "Ask about what?"
        choices = [ "wound", "time of death" ]
        
        Game.inputADV(line, choices)
        
        try:
            index = int(Game.input) - 1
            if index == 0:
                line = "Detective, please. Spare a grieving widow the gruesome details. {i}While her words are remorseful, her flat expression and wry tone suggest she's not too distraught by recent events.{/i}"
                choices = [ "Pressure", "Ask something else" ]
                
                inputDone = False
                while not inputDone:
                    character.inputADV(line, choices)
                
                    try:
                        index = int(Game.input) - 1
                        if index == 0:
                            inputDone = True
                            character.speakADV("{i}Her demeanour becomes even icier than before.{/i} Detective, while it is no secret that my husband and I were very much not in love, if all it took was one social dinner turned awkward by his bluster for me to decide to end his life, he would not have survived our first month of marriage. Now cease this insulting line of inquiry, and leave me be.")
                            Game.jump("start")
                        elif index == 1:
                            inputDone = True
                            Game.jump(character.label + "_loop")
                        else:
                            raise ValueError()
                    except ValueError:
                        Game.narrateADV("Invalid Input")
                        
            elif index == 1:
                pass
            else:
                raise ValueError()
                
        except ValueError:
            character.sayADV("I don't know what you mean.")
        
        Game.jump(character.label + "_loop")
label t_queen_other:
    python:
        line = "Who?"
        choices = []
        
        for npc in Game.npcs:
            if npc != character:
                choices.append(npc.name)
                
        # say line and give options
        Game.inputADV(line, choices)
        Game.checkQuit()
        
        try:
            index = int(Game.input) - 1
            choice = choices[index].lower()
            
            Game.jump(character.label + "_" + choice)
            
        except ValueError:
            character.speakADV("I don't know who you mean")
            
        Game.jump(character.label + "_loop")
label t_queen_bishop:
    python:
        character.sayADV("A really long block of text" * 100)
        Game.jump(character.label + "_loop")
label t_queen_knight:
    python:
        Game.jump(character.label + "_loop")
label t_queen_pawn:
    python:
        Game.jump(character.label + "_loop")
label t_queen_rook:
    python:
        Game.jump(character.label + "_loop")
