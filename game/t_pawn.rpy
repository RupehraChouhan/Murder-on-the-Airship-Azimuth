label t_pawn:
    scene bg whiteImage
    show pawn
    with fade 
    stop music fadeout 2
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_PAWN]
        
        # NPC speaks
        Game.prevNarrate = "What do you want me to say"
        Game.jump(character.label + "_loop")
        
label t_pawn_loop:
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
        
label t_pawn_you:
    python:
        character.speakADV("Name's Polly, Detective. Polly Newport. I'm the ships steward - have been for eight months.")
        Game.jump(character.label + "_loop")
label t_pawn_vic:
    python:
        character.speakADV("Mr. Royaume owns this ship. Owns a whole fleet of them. He flies on them plenty. For free of course.")
        Game.YOU.speakADV("So you've met him before.")
        character.speakADV("Yes, he's flown with us a few times.")
        Game.jump(character.label + "_loop")
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(Game.prevNarrate, choices)
        
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Had any trouble with him?")
            character.speakADV("It doesn't mean I killed him or nothing, but... ")
            character.speakADV("Whenever he flew with us, he treated us, me especially, like servants! I mean, we are basically servants, but we have shipboard duties! Can't spare the time to wait on him hand and foot, but try telling him that! If he wants that kind of attention, buy his butler a ticket, or hire us a proper service crew. ")
            character.speakADV("Every time he came aboard, I get dressed down by Captain Winfarthing.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")

label t_pawn_saw:
    python:
        character.speakADV("After dinner, I tried to tidy up, but Mr. Royaume had me waiting on him. Kept demanding I bring him this and that - brandy, cigars, whatever. We serve coffee and cigars at 9:30, but he had to have it right away. I finally got away after about half an hour, had to make my report to Captain Winfarthing, but she was fighting that storm. I tried to lend a hand on the bridge until it blew over, but then I had to get back to work back in service.")
        character.speakADV("A bit later, I went off to tell everyone that coffee and cigars were served. I couldn't find everyone, so I tried the baths. That's when I... found him.")
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(Game.prevNarrate, choices)
        
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("There are some gaps in your story, Miss.")
            character.speakADV("Wh- what do you mean?")
            Game.YOU.speakADV("Well, for instance, where did you go when you left the cockpit?")
            character.speakADV("Um, well, I had lots of work to catch up on, so I... I don't really -")
            character.speakADV("The bar! They'd made a mess of the bar, had to get that squared away. Which was tough with Rector Esgob there constantly asking me to pour him another.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
        
label t_pawn_found:
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
            line ="I - I already saw... that. Dunno where the murderer could've put hands on something big and heavy. All the tools in the engine room are locked up."
            choices = [ "Pressure", "Ask something else" ]
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("But you have a key, no? Or could get one?")
                character.speakADV("No, I'm in service, not engineering! Do you...? Are you saying I killed him?")
                character.speakADV("I - I'm gonna go to prison! If I ever get out, I'll never find respectable work again! I'll have to work at the grommet foundry for eighteen hours a day just to put watery gruel on the table! Just like my kid brothers!")
            elif index == 1:
                pass
            
        elif clueName == Game.BATHS_TIME_OF_DEATH:
            line = "Between 8:30 and 9? Working, playing catchup. On the bridge or in the bar, don't rightly remember. "
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("You don't {i}remember{/i}")
                character.speakADV("Detective, I've been running ragged for over a full day, getting this ship in order to host the owner of the line and his honoured guests. It's all running together. Then I found a dead body. I'm... I'm not at my best right now. Would you mind coming back when I'm a little more... collected?")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.GALLEY_PIPE:
            line = "A pipe out one of those contraptions keeps us flying? Maybe it was someone in engineering. Everyone has to work triple shifts when we get a dignitary flight, not just us in service. Could get to anyone."
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Of the suspects I am considering, you have the greatest knowledge of - and access to - this vessel...")
                character.speakADV("Do you...? Are you saying I killed him?")
                character.speakADV("Of course it's the poor girl who gets the rap! I - I'm gonna go to prison! If I ever get out, I'll never find respectable work again! I'll have to work at the grommet foundry for eighteen hours a day just to put watery gruel on the table! Just like my kid brothers!")
                Game.jump("start")
            elif index == 1:
                pass
                
        elif clueName == Game.CABINS_EMPTY:
            character.speakADV("You figure the weapon has to be hidden somewhere on the ship? Makes sense, I guess. I do know an out-of-the-way corner in the kitchen. Behind the ovens, there's a vent with a missing screw. Try looking in there?")
            character.speakADV("Don't tell the captain I knew that.")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("You know plenty about how to keep secrets on this vessel...")
                character.speakADV("Do you...? Are you saying I killed him?")
                character.speakADV("I didn't have to tell you that! I helped you! I risked my job - if the captain finds out I knew where to stash contraband...")
                character.speakADV("I'll never find respectable work again! I'll have to work at the grommet foundry for eighteen hours a day just to put watery gruel on the table! Just like my kid brothers!")
                Game.jump("start")
            elif index == 1:
                pass
                
        elif clueName == Game.DINING_SPECTACLES:
            line = "The Rector's glasses, sure."
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("When you saw him, was he wearing them?")
                character.speakADV("Not when he left the table at dinner. Though I did see him wearing them, when was that...?")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.LOUNGE_CONTRACTS:
            line = "That's all beyond me. I can read, not like most of my family, but that's a far cry from reading solicitor language."
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Would it surprise you to learn that Mr. de la Roque actually prepared most of these?")
                character.speakADV("Mr. de la Rocque was always scribbling something, so not really. What does that have to do with Mr. Royaume?")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.GALLEY_BOOK:
            Game.narrateADV("{i}Newport visibly starts when you show her the pamphlets.{/i}")
            character.speakADV("N - Never seen those before. What are they?")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("I think you just lied to me, miss.")
                Game.narrateADV("{i}Miss Newport looks panicked.{/i}")
                character.speakADV("Please, Detective! Don't tell anyone you found those! I was just... I'm no revolutionary! I just have... friends that go to the meetings! And sometimes... I go along. Just as a thing to do with friends, you know?")
                character.speakADV("If you tell the captain you found those, we'll all lose our jobs! Which sort of proves Singer's point, that the bourgeoisie don't care about the well-being of the workers, but - ")
                character.speakADV("Please, Detective! I'm begging you to keep those a secret!")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.CARGO_RECORD:
            line = "So the war hero is actually a war herO? Good to know."
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(line, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("He was at the Battle of Rosenfeldt.")
                Game.narrateADV("{i}Newport's eyes widen.{/i}")
                character.speakADV("I heard about that. So many dead. Miss Osgoode down the road from my parents lost her son Danny.")
                Game.narrateADV("{i}Newport gasps{/i}")
                character.speakADV("What if that's why he did it? What if he wanted revenge on the man who built the blimps? What if he wants revenge on all blimps?")
                character.speakADV("Detective, you have to lock him up, right away!")
                Game.jump("start")
            elif index == 1:
                pass
            
        elif clueName == Game.ROOK_BODY:
            Game.narrateADV("{i}Newport gasps{/i}")
            character.speakADV("Another murder? What if it's one of those slasher madmen like the one that terrorized Chapel Street last year? They never caught him!")
            choices = [ "Pressure", "Ask something else" ]
            
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("I am inclined to believe these killings have sensible motives, Miss. Like, for instance, a desire to effect a change to the management of Royaume & Sons Airship Lines...")
                character.speakADV("Do you...? Are you saying I killed him?")
                character.speakADV("Of course it's the poor girl who gets the rap! I - I'm gonna go to prison! If I ever get out, I'll never find respectable work again! I'll have to work at the grommet foundry for eighteen hours a day just to put watery gruel on the table! Just like my kid brothers!")
                Game.jump("start")
            elif index == 1:
                pass
            
        else:
            character.speakADV("I don't know what you're talking about.")
        Game.jump(character.label + "_loop")
        
label t_pawn_other:
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
        
label t_pawn_bishop:
    python:
        character.speakADV ("I've heard some of Rector Esgob's speeches on the televox. Seems like he knows how harsh it is, what the workers go through. Doesn't seem like he's had much success actually changing things, though. Asking nicely doesn't work too well, who'd have thought?")
        choices = [ "Pressure", "Ask something else" ]
            
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Can you think why a man like that would have reason to commit murder?")
            character.speakADV("Well, him and Mr. Royaume did get in a terrible row at dinner. Difference of politics, I'd expect. I was working, mostly hoping they didn't break any of the good dishes. I didn't really listen in, sorry.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
        
label t_pawn_knight:
    python:
        character.speakADV("Never met Sergeant-Major Ritter before. At least he's polite and tidies up after himself.")
        choices = [ "Pressure", "Ask something else" ]
            
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Could he possibly have had anything against Mr. Royaume?")
            character.speakADV("Wouldn't know, me. Doesn't seem like the Sergeant-Major talks much.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
label t_pawn_rook:
    python:
        character.speakADV("Mr. de la Rocque? I saw him whenever Mr. Royaume travelled with us. They were inseperable. Always had his head in a ledger. I didn't mind. He was much less demanding than Mr. Royaume.")
        choices = [ "Pressure", "Ask something else" ]
            
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Can you think of a reason Mr. de la Rocque might have had to murder Mr. Royaume?")
            character.speakADV("Royaume was a hard man to work under. I found him tough to put up with only seeing him a few days a year. I can't imagine what it was like every day of the week!")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
        
label t_pawn_queen:
    python:
        character.speakADV("She's as much a terror as her husband! They're rich, they've got servants at home. Why not bring them with them? Some of us have work to do, can't be running every errand that enters her head!")
        choices = [ "Pressure", "Ask something else" ]
            
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Do you think she could have any connection to the murder?")
            character.speakADV("I dunno. She didn't travel with us as much as her husband, thank goodness. Seems like they weren't that close, though. Heard them fighting before. Seemed like just a typical married couple row, though.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
