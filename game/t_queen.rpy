label t_queen:
    scene bg whiteImage
    show queen
    with fade 
    stop music fadeout 2
    
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_QUEEN]
        
        # NPC speaks
        Game.jump(character.label + "_loop")
        
label t_queen_loop:
    python:
        # define line and give options
        line = "What would you like to talk about?"
        choices = ["Tell me about yourself.", "What is your connection to the victim?", "Describe what you saw this evening", "Ask about a discovery", "Ask about another suspect", "Leave"]
        
        # say line and give options
        #character.speakADV(line)
        character.inputADV(line, choices)
        Game.checkQuit()
        
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
        
label t_queen_you:
    python:
        character.speakADV("You have the honour of addressing Her Ladyship Eleanora Francesca van Koenigen Royaume. The Widow Royaume, I suppose I shall have to become accustomed to being called.")
        Game.jump(character.label + "_loop")
label t_queen_vic:
    python:
        line = "My 'connection'? We are - were -  married fourteen years."
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(line, choices)
        
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("No children?")
            character.speakADV("It's no secret my husband and I weren't close. And, yes, before you ask, I do stand to inherit a large sum of money, which, yes, will revitalize the long-flagging van Koenigen family fortune. I still didn't kill him.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
label t_queen_saw:
    python:
        character.speakADV("After Henry and Rector Nathaniel had that wearisome row at dinner, I repaired to the bar for a glass of the only barely-passable brandy this undignified air-carriage has to offer.")
        character.speakADV("The steward was nowhere bo be found; I had to serve myself, can you believe that? At least until Rector Esgob showed up moments later. He was more than happy to top me up in between each three or four glasses he downed himself.")
        character.speakADV("His company quickly became tiring. I withdrew to the galley of all places at around half-past-eight so I might enjoy some solitude. At about nine, I heard someone approaching - likely the staff, finally getting back to work - so I relocated to the passenger lounge for about half an hour. I intended to enjoy a bite of torte in the dining room before retiring, but I was dragged into yet another conversation with Esgob there.")
        character.speakADV("I only managed to politely excuse myself by 9:30 and encountered Sergeant-Major Ritter near the cockpit. Now there's a man who knows how to not aggravate everyone near him. The world needs more like him. We were taking in the view in silence when that ghastly shriek rang out.")
        
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Are you sure that's all you witnessed?")
            character.speakADV("Detective, why would I conceal anything? The blow to my reputation from a drawn-out and scandalous investigation would be personally devastating. It's in my interest that you resolve this... unpleasantness... quickly and discreetly.")
        elif index == 1:
            pass
        
        Game.jump(character.label + "_loop")
label t_queen_found:
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
            line = "Detective, please. Spare a grieving widow the gruesome details. {i}While her words are remorseful, her flat expression and wry tone suggest she's not too distraught by recent events.{/i}"
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                character.speakADV("{i}Her demeanour becomes even icier than before.{/i} Detective, while it is no secret that my husband and I were very much not in love, if all it took was one social dinner turned awkward by his bluster for me to decide to end his life, he would not have survived our first month of marriage. Now cease this insulting line of inquiry, and leave me be.")
                Game.jump("start")
            elif index == 1:
                Game.jump(character.label + "_loop")
        elif clueName == Game.BATHS_TIME_OF_DEATH:
            character.speakADV("Between 8:30 and 9? I recall the clock in the galley chiming the quarter hour. Only place I could find some solitude on this miniscule vessel.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("You were alone that whole time?")
                character.speakADV("Yes. I'd had quite enough of these fatuous, up-jumped {i}nouveaux riches{/i} that my husband has seen fit to provide with the gift of flight, and below stairs was the only place I could be assured of not encountering them.")
            elif index == 1:
                Game.jump(character.label + "_loop")
        elif clueName == Game.GALLEY_PIPE:
            pass
        elif clueName == "Ask something else":
            Game.jump(character.label + "_loop")
        else:
            character.speakADV("I don't know what you're talking about.")
        
        Game.jump(character.label + "_loop")
        
label t_queen_other:
    python:
        line = "Who?"
        choices = []
        
        for npc in Game.npcs:
            if npc != character:
                choices.append(npc.name)
                
        # say line and give options
        Game.inputADV(line, choices, True)
        Game.checkQuit()
        
        index = int(Game.input) - 1
        choice = choices[index].lower()
            
        Game.jump(character.label + "_" + choice)

label t_queen_bishop:
    python:
        character.speakADV("A really long block of text" * 100)
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
