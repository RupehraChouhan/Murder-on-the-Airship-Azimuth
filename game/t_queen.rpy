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
                pass
        elif clueName == Game.BATHS_TIME_OF_DEATH:
            character.speakADV("Between 8:30 and 9? I recall the clock in the galley chiming the quarter hour. Only place I could find some solitude on this miniscule vessel.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("You were alone that whole time?")
                character.speakADV("Yes. I'd had quite enough of these fatuous, up-jumped {i}nouveaux riches{/i} that my husband has seen fit to provide with the gift of flight, and below stairs was the only place I could be assured of not encountering them.")
            elif index == 1:
                pass
        elif clueName == Game.GALLEY_PIPE:
            character.speakADV("Is that all you wished to communicate? That my husband's skull was bashed in with a length of pipe? What possible further insight could I offer you?")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("If I could just - ")
                character.speakADV("Detective, if you are being deliberately grotesque to provoke a reaction in me, I must say you have succeeded brilliantly. Good day.")
                Game.jump("start")
            elif index == 1:
                pass
        elif clueName == Game.CABINS_EMPTY:
            character.speakADV("You've already been indecorous enough to sift through my belongings. I travel aboard these wretched contraptions of my - late - husband's as little as possible. I wouldn't have the faintest clue where to conceal a weapon, and I'm not sure I appreciate the insinuation.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("No insinuation, I just wondered if you had noticed any out-of-the-way corners during your voyage.")
                character.speakADV("Isn't ferreting out hidden corners {i}your{/i} chosen vocation? Perhaps ask someone in service; I'm of no use to you.")
            elif index == 1:
                pass
        elif clueName == Game.DINING_SPECTACLES:
            character.speakADV("Esgob's spectacles. Their inexpensive workmanship and lingering aroma of self-righteousness are unmistakeable.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("When you saw him, was he wearing them?")
                character.speakADV("Now that you mention it, no. I recall him squinting to read the labels in the bar after dinner. He was wearing them when I saw him later in the dining room, though.")
            elif index == 1:
                pass
        elif clueName == Game.LOUNGE_CONTRACTS:
            character.speakADV("I'm afraid I stayed well out of my husband's business, Detective. An aristocrat doesn't stoop to {i}commerce{/i}.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Would it surprise you to learn that Mr. de la Roque actually prepared most of these?")
                Game.narrateADV("{i}Lady Eleanora pauses for a moment.{/i}")
                character.speakADV("No. Mr. de la Roque always struck me as more capable and less frivolous than my husband. Henry was very talented at taking credit for others' actions.")
            elif index == 1:
                pass
        elif clueName == Game.GALLEY_BOOK:
            character.speakADV("That repulsive drivel that plays so well with the underclasses actually capable of reading? I don't see what that has to do with me. Besides, I'm personally thankful that Mr. Singer has drawn the ire of the masses toward the capitalists and away from the aristocracy.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("It might have something to do with your husband's death. Would any of your fellow passengers be at all receptive to this kind of ideology?")
                Game.narrateADV("{i}Lady Eleanora considers your question for a moment.{/i}")
                character.speakADV("Well, Esgob is a crass populist at heart, but I doubt he's this radical. Ritter's misadventures in service to the Crown have not dulled his patriotism at all. And de la Rocque is the precise kind of industrialist this screed incites violence against. It is crafted to appeal with the lowest among us, Detective.")
            elif index == 1:
                pass
        elif clueName == Game.CARGO_RECORD:
            character.speakADV("Thanks to an aristocratic education, if there's one subject I'd like to peruse less than geneaology, it's records of military accomplishments.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Did you know that Sergeant-Major Ritter's decorations arise from surviving a bombing facilitated by one of your husband's zeppelins?")
                Game.narrateADV("{i}Lady Eleanora is silent for a moment.{/i}")
                character.speakADV("I did not. Perhaps you should speak to him about this.")
            elif index == 1:
                pass
        elif clueName == Game.ROOK_BODY:
            character.speakADV("A grave tragedy. To lose my husband and a dear family friend all in one evening. Detective, I implore you, find this killer. I fear I may be next.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("With your husband and his business partner now dead, I understand control of Mr. Royaume's company falls to you...")
                character.speakADV("Your implications are frankly insulting, Detective! I have entertained your tedious questions long enough! Go and earn your reputation instead of pestering your betters. Leave my presence at once!")
                Game.jump(character.label + "_loop")
            elif index == 1:
                pass
        
        elif clueName == "Ask something else":
            pass
        else:
            character.speakADV("I don't know what you're talking about.")
        
        Game.jump(character.label + "_loop")
        
label t_queen_other:
    python:
        line = "Who?"
        choices = []
        
        for npc in Game.npcs:
            if npc != character and npc.alive:
                choices.append(npc.name)
                
        # say line and give options
        Game.inputADV(line, choices, True)
        Game.checkQuit()
        
        index = int(Game.input) - 1
        choice = choices[index].lower()
            
        Game.jump(character.label + "_" + choice)

label t_queen_bishop:
    python:
        character.speakADV("Rector Esgob, the social reformer? A pitiable man. Why these organizations of {i}tradespeople{/i} have seen fit to fund his speaking tour of Her Infallible Majesty's dominions is beyond me. You should have heard his mawkish anecdotes about \"the plights of the working classes\" at dinner. An unseemly topic for a polite occasion.")
        character.speakADV("Normally, I'm {i}wearied{/i} when Henry starts a row at dinner, but in this case, it was warranted.")
        
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("So Esgob and your husband argued?")
            character.speakADV("Yes. Esgob apparently took issue with Henry's charitable efforts to offer factory work to impoverished children. Better they learn how to rivet an airship than how to pick a pocket, I say.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
label t_queen_knight:
    python:
        character.speakADV("Ritter, the Sergeant-Major? Such a gentleman! Somewhat taciturn, but better that than boorish.")
        
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Could he possibly have had anything against your husband?")
            character.speakADV("As far as I know, they'd never met before dinner. Why are you asking me?")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
label t_queen_pawn:
    python:
        character.speakADV("Who's Polly Newport? Oh, the steward? A disgrace. I recommended Henry have her let go after she refused - refused! - to fetch my hatbox from the hold. I'm not interested if it's \"lashed up tight\" or whatever colourful idiom she used - you're in service, so you serve.")
        
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Do you think she could have any connection to the murder?")
            character.speakADV("Very possibly. She had quite the superior tone. Thoughts far above her station.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
label t_queen_rook:
    python:
        character.speakADV("de la Rocque? My husband's solicitor and business partner. From how I understand it, Henry handled the large-scale direction and public image of the firm, while Mr. de la Rocque fussed with sums and the tiresome minutiae.")
        character.speakADV("They've been colleagues for years. Often times Mr. de la Rocque would see more of Henry than I would. These past weeks have certainly been one of those times, what with this government contract and all.")
        
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Could he possibly have had anything against your husband?")
            character.speakADV("As far as I know, they'd never met before dinner. Why are you asking me?")
        Game.jump(character.label + "_loop")
