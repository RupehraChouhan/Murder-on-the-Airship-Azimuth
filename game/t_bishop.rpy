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
        Game.narrateADV("{i}Esgob steadies himself. His face is flushed and he reeks of liquor. Despite this, his eyes are lucid and frightened. Perhaps the shock has sobered him up.{/i}")
        character.speakADV("Rector Nathaniel Esgob, of the Compassionate Reform Crusade.")
        Game.YOU.speakADV("And what is that?")
        character.speakADV("It's a social movement. We're seeking, well, um, compassionate reform. Particularly in our nation's industrial sites. Seeking to ban child labour, encouraging temperance, that kind of thing.")
        Game.jump(character.label + "_loop")

label t_bishop_vic:
    python:
        character.speakADV("We hadn't met in person before. I've written him many letters, talking about the deplorable conditions in his factories... I always received very noncommittal replies, usually from the desk of Mr. de la Rocque.")
        character.speakADV("I doubt Royaume even read them.")
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(line, choices)
        
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("That must have been frustrating.")
            character.speakADV("Detective, I see what you're implying! I didn't kill him. I-I couldn't ever even think of such a thing! I'm a pacifist, for heaven's sake! Ask me your questions when you're several degrees more sensible!")
            Game.jump(character.label + "_loop")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")

label t_bishop_saw:
    python:
        character.speakADV("After dinner, I - uh, I retired to my room for a spell. Then I went back to the dining room. I, um, had forgot my reading glasses. That was about 8:30. Then I must have got turned around, I ended up in the bar at 9. The steward was tidying up when I arrived. She invited me for coffee and cigars in the dining room at 9:30, which I had just sat down to enjoy when I heard her scream! Mr. de la Rocque and I went running, and we found her staring in shock at that poor man...")
        choices = ["Pressure","Ask something else"]
        character.inputADV(Game.prevNarrate, choices)

        index = int(Game.input) - 1
        if index ==0:
            Game.YOU.speakADV("Anything you'd like to add?")
            character.speakADV("I'm not sure what you mean.")
            Game.YOU.speakADV("I don't think you're telling me everything.")
            Game.narrateADV("{i}Esgob visibly shakes.{/i}")
            character.speakADV("You're right! I didn't go to my cabin after dinner! I stopped in the bar. It calms my nerves! I've never flown before, it's quite alarming! Please don't tell my supporters in the temperance movmement!")
            Game.YOU.speakADV("Why did you lie to me, Rector?")
            character.speakADV("I... Lady Eleanora was there, and I'd just argued with Mr. Royaume, and I... I thought it would appear unseemly if I admitted to drinking with another man's wife shortly before he turned up dead.")
            Game.YOU.speakADV("More unseemly than being caught lying to the detective trying to solve that murder?")
            character.speakADV("Are you even attached at all to the police?")
            Game.YOU.speakADV("No, I am merely an accomplished amateur.")
            character.speakADV("Then I don't have to answer any more of your questions.")
            Game.jump(character.label + "_loop")
        elif index ==1:
            pass
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
            line = "Oh, how dreadful. A heavy bludgeon, you say? Haven't seen anything like that."
            choices = ["Pressure", "Ask someone else"]

            character.inputADV(line,choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Are you quite certain? It's a large ship...")
                character.speakADV("Yes, I'm certain!")
                Game.narrateADV("{i}Esgob regains his composure and looks up at you, worriedly. He holds out a shaking hand.{/i}")
                character.speakADV("Look at this, Detective. Shaking like a leaf. I've been a nervous wreck since we came aboard. First time flying. Do you think I have the strength to swing such a thing?")
                Game.jump("start")
            elif index == 1:
                pass
        elif clueName == Game.BATHS_TIME_OF_DEATH:
            character.speakADV("Between 8:30 and 9 I was in the dining room. I'd misplaced my spectacles. They - aheh - they took some finding.")
            Game.narrateADV("{i}Rector Esgob is not currently wearing spectacles.{/i}")

            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("You're not wearing them now.")
                Game.narrateADV("{i}Esgob pats his breast pockets.{/i}")
                character.speakADV("Oh, blast. Mislaid them again. Where could they be this time?")
                Game.YOU.speakADV("Also, do you expect me to believe it takes a whole half-hour to find your spectacles?")
                character.speakADV("I suspect some assiduous servant moved them. Somewhere. If you were half as assiduous, you'd be finding a killer, not haranguing me about my spectacles!")
                Game.jump(character.label + "_loop")

            elif index == 1:
                pass
        elif clueName == Game.GALLEY_PIPE:
            character.speakADV("Oh, how ghastly!")

            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("It was found in the galley. Any chance you passed by there earlier?")
                character.speakADV("Detective, I've accounted for my whereabouts! Have I lied to you yet?")
                Game.YOU.speakADV("Probably.")
                character.speakADV("This isn't amusing, Detective. I have tried my best to help you do the right thing and you insist on bedeviling me! Return when you see fit to take this seriously!")
                Game.jump(character.label + "_loop")

            elif index == 1:
                pass
        elif clueName == Game.CABINS_EMPTY:
            character.speakADV("I'm afraid I'm not much use in finding hidden corners, Detective. I misplaced my spectacles earlier tonight.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Indulge me for a moment, Rector. Imagine I'm the murderer. I strike Mr. Royaume in the baths, there's blood on my hands, I search around for a hiding place. Where do I look?")
                character.speakADV("I- I wouldn't know! I've never even seen a dead body! Read about them plenty. Besides, it's my first time on one of these wretched skyships! I wouldn't know what to look for!")
            elif index == 1:
                pass

        elif clueName == Game.DINING_SPECTACLES:
            character.speakADV("Ah, you found my spectacles! Thank you!")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("I found them in the dining room. You said you already found them there.")
                character.speakADV("Well, yes. Then I went back later. They were, ah, serving coffee. I must have... lost them again. Then. There.")
            elif index == 1:
                pass
        elif clueName == Game.LOUNGE_CONTRACTS:
            character.speakADV("I'm afraid this sort of thing is beyond me. I've helped draft charters of labour rights, but I kept the language plain. You know. For the working classes.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Is it fair for me to say you were against this deal?")
                character.speakADV("Yes, all it means is more money in the pockets of Royaume while his workers suffer in intolerable conditions! Perhaps his partner, de la Rocque will be more amenable to reform...")
                Game.narrateADV("{i}It dawns on Esgob what he is saying.{/i}")
                character.speakADV("I - I didn't mean it like that! Maybe - maybe you should come back later, Detective. When I've had a chance to collect myself.")
                Game.jump(character.label + "_loop")
            elif index == 1:
                pass

        elif clueName == Game.GALLEY_BOOK:
            character.speakADV("I'm no Singerist! Of course we both want better conditions for workers, but revolution isn't the answer! Surely, by appealing to industrialists' sense of humanity, by showing them the conditions that exist in their factories...")
            character.speakADV("That's beside the point. What does it have to do with the... killing, though?")

            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("I was hoping you might tell me.")
                character.speakADV("Detective, my objections to the maltreatment of workers are moderate and pacifistic. Singer's call for violent revolution does the workers more harm than good. You're barking up the wrong tree. Find that book's owner, you'll find a madman with a motive.")
            elif index == 1:
                pass

        elif clueName == Game.CARGO_RECORD:
            character.speakADV("Very impressive, I'm sure. I value his service, even if I object to our involvement in foreign wars.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Ritter was at the battle of Rosenfeldt. Does that mean anything to you?")
                character.speakADV("I understand it was a disaster, but I don't know much else. My area of expertise is {i}domestic{/i} suffering, I'm afraid.")
            elif index == 1:
                pass

        elif clueName == "Ask something else":
            pass
        else:
            character.speakADV("I don't know what you're talking about.")
        Game.jump(character.label + "_loop")
label t_bishop_other:
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

label t_bishop_rook:
    python:
        character.speakADV("Not to speak ill of the dead, but de la Rocque is much more agreeable than Mr. Royaume. Very diplomatic. I gather he didn't care much for me, but he at least took the time to listen. I had thought... Never mind.")
        
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("In your estimation, could he be responsible for the murder?")
            character.speakADV("You know, he could be! It takes a particularly immoral man to express sympathy at my letters about his workers' suffering but do nothing to alleviate it. I had thought it was just because he was the junior partner, without any real power, but now that you mention it... Hmmmm.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")

label t_bishop_knight:
    python:
        character.speakADV("I don't know much about Sergeant-Major Ritter. We'd never met before, and he's quite taciturn.")

        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("In your estimation, is he capable of murder?")
            character.speakADV("Well. He is the only one here who has killed before. In service to the Crown, for sure, but... No. He's an honourable man, I'd say.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")

label t_bishop_pawn:
    python:
        character.speakADV("I can't believe Miss Newport is under investigation. She's as dedicated as any on this crew. She was putting in extra effort to see we were well cared-for.")
        
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Maybe that wasn't dedication. Maybe that was fear.")
            character.speakADV("Fear? Fear of what?")
            Game.YOU.speakADV("Losing her post.")
            character.speakADV("If she didn't wait on us upper-crust passengers, you mean? It's very possible. There's always more desperate souls looking for work that isn't the factories. I have no trouble believing Royaume would fire her in an instant if someone who'd do more work for less came along.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")

label t_bishop_queen:
    python:
        character.speakADV("Lady Eleanora is charming, of course, but has no conception of the plights of the masses, as most of her aristocratic peers don't.")
       
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Do you think she's capable of murder?")
            character.speakADV("Detective, if you'd asked me this afternoon, I'd have said none of us is capable of murder... Are we certain it wasn't an accident?")
        Game.jump(character.label + "_loop")