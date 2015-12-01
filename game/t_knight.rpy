init 0 python: # knight conversation related state
    Game.state[Game.CONV_KNIGHT_WHAT] = False

label t_knight:
    stop music fadeout 2
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_KNIGHT]
        
        # NPC speaks
        Game.prevNarrate = "What do you want me to say"
        Game.jump(character.label + "_loop")
        
label t_knight_loop:
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
        
label t_knight_you:
    python:
        character.speakADV("Sergeant-Major Angus P. Ritter, Her Infallible Majesty's Ninth Overland Rifle Brigade, retired. ")
        Game.jump(character.label + "_loop")
        
label t_knight_vic:
    python:
        line = "I was invited by Mr. Royaume's solicitor, Mr. de la Rocque, to consult on the finer points of Royaume's contracts with the Admiralty. Mr. Royaume was surprised by my presence. It seems Mr. de la Rocque handles the business. I had never met Mr. Royaume before this voyage."
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(line, choices)
        
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("That was the extent of your connection?")
            character.speakADV("Detective, I am - was - an enlisted man. I don't move in these circles. My whole life and career is on record. Check my papers if you don't believe me. They're in my red trunk in the cargo hold. I have nothing to hide.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
        
label t_knight_saw:
    python:
        Game.state[Game.CONV_KNIGHT_WHAT] = True
    
        character.speakADV("I left the dining table at eight o'clock precisely. I recovered a book from my luggage in the hold, then returned to my cabin, where I remained until 9:30.")
        character.speakADV("At that time, I visited the observation deck near the cockpit, where I encountered Lady Royaume. We observed the night sky in silence until Airman Newport discovered the body.")
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(Game.prevNarrate,choices)
        index = int(Game.input)-1
        if index == 0:
            Game.YOU.speakADV("That was very succinct, thank you.")
            Game.narrateADV("{i}Ritter nods sharply{/i}")
            Game.YOU.speakADV("Anything else?")
            character.speakADV("No.")
            Game.YOU.speakADV("Alright then.")
        elif index == 1:
            pass
        
        Game.jump(character.label + "_loop")

label t_knight_found:
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
            line = "From the look I got, I'd agree. A decent length of steel, you don't need much strength to crack a man's skull."
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("You seem to know a lot about this.")
                character.speakADV("I was a soldier, Detective. I've seen killing. War's not clean, like they make it look in the paintings.")
                Game.narrateADV("{i} Ritter gives you a long, level stare.{\i}")
                character.speakADV("I didn't kill him, Detective. I didn't even know him.")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.BATHS_TIME_OF_DEATH:
            line = "Between 8:30 and 9 I was in my cabin. Alone. "
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Did you see anything, hear anything?")
                character.speakADV("No, I'm afraid not, Detective.")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.GALLEY_PIPE:
            line = "Found it, did you?"
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("You seem awfully collected about this whole affair.")
                character.speakADV("How precisely should I react, Detective? I've seen men die before. More even than you in your illustrious career. If suspicious insinuations and your intuitions about character are the extent of your investigative skills, I am appalled that your reputation is as great as it is.")
                Game.jump("start")
            elif index == 1:
                pass
                
        elif clueName == Game.CABINS_EMPTY:
            character.speakADV("I will say this for Royaume's ships - they are efficient. Very little wasted space and material, even in these ostentatious luxury decks. I haven't noticed anywere one could hide a weapon, Detective, I'm sorry.")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Indulge me for a moment, Sergeant-Major. Imagine I'm the murderer. I strike Mr. Royaume in the baths, there's blood on my hands, I search around for a hiding place. Where do I look?")
                character.speakADV("I'm afraid I can't help you. Cowardly attacks such as this are not a soldier's specialty. I suggest you ask these questions of someone with something to gain from Mr. Royaume's death. [END]")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.DINING_SPECTACLES:
            character.speakADV("Esgob's spectacles. What of them?")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("When you saw him, was he wearing them?")
                character.speakADV("At dinner, yes. I didn't see him again until the body was found.")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.LOUNGE_CONTRACTS:
            character.speakADV("I've already seen these. Mr. de la Rocque asked me to consult on the language, you know. He thought the sponsorship of a decorated soldier might aid him in dealing with the Admiralty.")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Confidentially, is there anything untoward about this deal?")
                character.speakADV("I think it's misguided. I think it's naked profiteering. But it's entirely above-board, legally speaking. ")
                Game.YOU.speakADV("Did you mention your reservations to Royaume?")
                character.speakADV("Based on those documents, it's de la Rocque to whom I should have brought them. Every word of them save the signatures was his. ")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.GALLEY_BOOK:
            character.speakADV("I don't get involved in politics. I have dedicated my life to service of Her Infallible Majesty's government, whatever that government may be.")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("It might have something to do with Royaume's death. Would any of your fellow passengers be at all receptive to this kind of ideology?")
                Game.narrateADV("{i}Ritter gives you a level stare.{/i} ")
                character.speakADV("I said I don't get involved in politics.")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.CARGO_RECORD:
            character.speakADV("My whole life is in there. Does that help answer your questions?")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("I understand you were at the Battle of Rosenfeldt?")
                Game.narrateADV("{i}Ritter draws a quick breath.{/i}")
                character.speakADV("And?")
                Game.YOU.speakADV("It says your regiment was decimated by airborne bombing. Friendly airborne bombing. From a Royaume-made war zeppelin. The same kind that Royaume is trying to sell to the Admiralty in quantity.")
                Game.narrateADV("{i}Ritter speaks through gritted teeth.{/i}")
                character.speakADV("Are you accusing me of murder, Detective?")
                Game.YOU.speakADV("That remains to be seen. [END]")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.ROOK_BODY:
            character.speakADV("Thank you for your concern, Detective, but I am unharmed. If the killer comes for me next, I am prepared to defend myself.")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("And if that killer is you, Sergeant-Major?")
                Game.narrateADV("{i}There is a long pause. Ritter's face is calm.{/i}")
                character.speakADV("Then I suppose you'd best lock me away, Detective. After you find some proof, that is.[END]")
                Game.jump("start")
            elif index == 1:
                pass
                
        else:
            character.speakADV("I don't know what you're talking about.")
            
        Game.jump(character.label + "_loop")
label t_knight_other:
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

label t_knight_bishop:
    python:
        character.speakADV("Rector Esgob, the social reformer? A principled man. Willing to defend those principles, if suppertime's heated debate was any indication.")
        choices = [ "Pressure", "Ask something else" ]
            
        character.inputADV(line, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Would he kill to defend those principles?")
            character.speakADV("I doubt it. The man's many things, but he's no hypocrite. That said, he did have a lot to drink. If he'd had a few more, there's no predicting what he'd do. ")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
        
label t_knight_rook:
    python:
        character.speakADV("de la Rocque, the solicitor? A diligent man. What about him?")
        choices = [ "Pressure", "Ask something else" ]
            
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("In your estimation, could he be responsible for the murder?")
            Game.narrateADV("{i}Ritter's brow furrows.{/i}")
            character.speakADV("I suppose. He's worked long in Royaume's shadow without a trace of ambition. But perhaps branching out into arms dealing has soured his morals some.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
        
label t_knight_pawn:
    python:
        character.speakADV("The steward? She seems dutiful enough. She insisted on attending to her duties even in the face of the Royaumes' demands for personal attention.")
        choices = [ "Pressure", "Ask something else" ]
            
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Could that have driven her to murder?")
            character.speakADV("Doubtful, in my opinion. She's rank-and-file. She's accustomed to those in charge not knowing what they're doing and giving her orders anyway. ")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
        
label t_knight_queen:
    python:
        character.speakADV("The Lady Eleanora? I've only just met her. She seems the picture of decorum.")
        choices = [ "Pressure", "Ask something else" ]
            
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Do you think she's capable of murder?")
            character.speakADV("She clearly did not love him. And I imagine she stands to inherit a fortune. Many more men have died for worse reasons.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
