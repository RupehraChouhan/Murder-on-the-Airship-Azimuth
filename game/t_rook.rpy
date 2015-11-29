label t_rook:
    stop music fadeout 2
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_ROOK]
        
        # NPC speaks
        Game.prevNarrate = "What do you want me to say"
        Game.jump(character.label + "_loop")
        
label t_rook_loop:
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
        
label t_rook_you:
    python:
        character.speakADV("My name is Charles Westinghouse de la Rocque, Esq. Please, how can I help you find the murderer?")
        Game.jump(character.label + "_loop")
label t_rook_vic:
    python:
        character.speakADV("I'm his business partner as well as his personal solicitor. The two of us made Royaume & Sons what it is today. I can't believe he's dead.")
        choices = [ "Pressure", "Ask something else" ]
        character.inputADV(line, choices)
        
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("With Mr. Royaume's passing, do I understand correctly that control over the business passes solely to you?")
            Game.narrateADV("(i)de la Rocque looks taken aback.(/i)")
            character.speakADV("Well, yes, but that's hardly reason to kill him! Henry was an excellent public face for the firm, something I've no talent for. It will take ages to recover from this!")
            character.speakADV("Though I am, of course, far more distraught over the loss of my friend. *Harrumph*.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
label t_rook_saw:
    python:
        character.speakADV(" After dinner, that storm was still raging, so I went to see how the crew was coping. It's one thing to read an engineer's blueprint, another to see it in action, you know? I wanted to have a word with the captain, but she was not in a position to speak at the time. She had the vessel well in hand, though.")
        character.speakADV("I retired to the passenger lounge and went over some papers until the storm passed. At 9, the storm had blown over, and I spoke with Captain Winfarthing. She will, of course, corroborate this. I then enjoyed the nuts and coffee in the dining room with Rector Esgob - much more composed, thankfully - until we heard that dreadful scream and went running.")
        choices = ["Pressure","Ask something else"]
        character.inputADV(choices)

        index = int(Game.input) - 1
        if index ==0:
            Game.YOU.speakADV("Are you sure that's all you witnessed?")
            character.speakADV("Well, I think so. Henry was headed to the lounge after dinner. He liked a good cigar after dinner. I didn't see him there when I came back through there later, 8:30 or so.")
        elif index ==1:
            pass
        Game.jump(character.label + "_loop")
label t_rook_found:
    python:
        line = "Ask about what?"
        choices = []

        for clueName, found in Game.cluesFound.items():
            if found:
                choices.append(cluename)
        choices.append("Ask something else")

        Game.inputADV(line, choices, True)

        index = int(Game.input) - 1
        cluename = choices[index]
        if clueName == Game.BATHS_WOUND:
            line = "Something heavy, eh? Unless a passenger brought the weapon aboard, it would have to be one of the pipe wrenches. They keep them in the engine room, and they're (i)supposed(/i) to all be locked up when not in use. Aside from that, I can't think of anything that fits the description. No extra weight on a Royaume ship! Well, except..."
            choices = ["Pressure", "Ask someone else"]

            character.inputADV(line,choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Except what?")
                character.speakADV("The engineers did insist that we install some redundancy in one of the machines. The responso-something baro-whatever. The names those people come up with.")
                Game.narrateADV("(i)Mr. de la Rocque shakes his head bemusedly.(/i)")
                Game.YOU.speakADV("Anyway, that thing has a few more pipes than it needs to keep running. On the inside, though.")
                Game.jump("start")
            elif index == 1:
                pass
        elif clueName == Game.BATHS_TIME_OF_DEATH:
            character.speakADV("Where was I between 8:30 and 9? I meant to be speaking with Captain Winfarthing, but she'd been busy with the storm, and I got caught up reviewing our contracts in the meantime.")

            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("You were alone that whole time?")
                character.speakADV("Yes, entirely. Oh, wait. I passed by the steward on one of my visits to the cockpit. She was coming from the lounge.")
            elif index == 1:
                pass
        elif clueName == Game.GALLEY_PIPE:
            Game.narrateADV("(i)de la Rocque's face twists uncomfortably(/i)")
            character.speakADV("How dreadful.")

            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("The use of this weapon implies a familiarity with this vessel that not everyone here has...")
                character.speakADV("Are you implying that I..? Detective, I've been nothing but helpful! I can't believe you'd... I think I'd like you to leave.[END]")
                Game.jump(character.label + "_loop")
            elif index == 1:
                pass
        elif clueName == Game.CABINS_EMPTY:
            character.speakADV("I worked closely with the engineers to cut down on awkward nooks - to save on materials and discourage transporing contraband, both. You say you've searched the cabins? Then it must be in plain sight somewhere, I'd stake my reputation on it.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Are you quite sure?")
                Game.narrateADV("(i)de la Rocque narrows his eyes.(/i)")
                character.speakADV("I would have thought the words, \"I'd stake my reputation on it\" were quite clear. After all, (i)your(/i) reputation is the only reason we're putting up with these invasive questions.[END]")
                Game.jump(character.label + "_loop")
            elif index == 1:
                pass
        elif clueName == Game.DINING_SPECTACLES:
            character.speakADV("Esgob's spectacles. What about them?")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("When you saw him, was he wearing them?")
                character.speakADV("Yes, he was wearing them at dinner. I seem to recall him taking them off when the nuts and coffee were served at 9:30.")
            elif index == 1:
                pass
        elif clueName == Game.LOUNGE_CONTRACTS:
            character.speakADV("Please, might I have those back? They're quite sensitive, you know. They pertain to imperial security.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("I note that it's your signatures on most of these.")
                character.speakADV("And?")
                Game.YOU.speakADV("I wonder if the recognition Mr. Royaume was receiving for all your hard work might have irritated you.")
                character.speakADV("Irritated me?! I'll tell you what irritates me! The implication from an amateur armchair sleuth such as yourself that I had anything to do with my colleague's murder! Yes, I did most of the work on this contract, and yes, I don't get invited to the same parties as Henry and Eleanora, and no, I'm not up for a knighthood for service to the Crown, but that doesn't mean I have to put up with your questions! [END]")
                Game.jump(character.label + "_loop")
            elif index == 1:
                pass
        elif clueName == Game.GALLEY_BOOK:
            character.speakADV("Where did you find those? We've made it quite clear that possession of Singer's writings is grounds for dismissal at any of our plants or on any of our vessels! Damn rabble-rouser. Singerists were responsible for a riot at our factory in the Esterlands last month. Had to hire some local help to break the strike.")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Do you think it could have played a part in your colleague's death?")
                character.speakADV("Absolutely. You find who owns that book, you find your killer. Whose is it? Esgob's? I knew that weepy, pious exterior was a front.We've had threats at the office, bricks through the window, it was only a matter of time before it was sabotage - or murder...")
            elif index == 1:
                pass
        elif clueName == Game.CARGO_RECORD:
            character.speakADV("Ritter is unsuaally tight-lipped about his escapades as an enlisted man. I'm sure it's fascinating reading, but is it relevant?")
            
            choices = ["Pressure", "Ask something else"]
            character.inputADV(Game.prevNarrate, choices)
            index = int(Game.input) - 1
            if index == 0:
                Game.YOU.speakADV("Did you know that Sergeant-Major Ritter's decorations arise from surviving a bombing facilitated by one of your company's zeppelins? The very same zeppelins you're intending to mass-produce for Her Infallible Majesty's government?")
                character.speakADV("The Rosenfeldt Incident? It was shoddy intelligence, everyone knows that! Nothing to do with the prototype war zeppelin! It performed its job perfectly! Human error on the part of military - not Royaume - personnel, he understands that, surely. These things happen in war!")
            elif index == 1:
                pass

        elif clueName == "Ask something else":
            pass
        else:
            character.speakADV("I don't know what you're talking about.")        
        Game.jump(character.label + "_loop")

label t_rook_other:
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
        
label t_rook_bishop:
    python:
        character.speakADV("This is confidential, yes? I have a dim view of Rector Nathaniel Esgob's reputation. His calls for compassionate reform, so-called, have led to pickets and stoppages at some of our factories. But we have to maintain the appearance that we entertain his outlandish schemes to coddle our workers. Otherwise, the Singerists get involved, and instead of pickets and stoppages, it's sabotage and firebombings. Madness.")
        character.speakADV("Anyway, a dozen or more tradesmen's federations put up the money to fund him on a speaking tour of the industrial towns down south, and we simply (i)had(/i) to agree. Naturally, though, it wasn't long before he started spouting his noxious opinions, and Henry had to set him straight.")
        
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("So Esgob and Mr. Royaume argued?")
            character.speakADV("Yes. And Esgob put up with his bluster better than most, believe me. I've been on the receiving end of that before, and it takes it out of you. Not to speak ill of the dead, of course.")
            character.speakADV("I imagine the liquid courage helped some. For a man so supported in the temperance movement, he sure had a lot of wine with dinner, before shuffling off to the bar, no less.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
  
label t_rook_knight:
    python:
        character.speakADV("I asked Sergeant-Major Ritter to attend personally. He wrote to my office when he heard rumour of our dealings with the government. We are in the final stages of drafting this contract for Her Infallible Majesty's Admiralty, and I thought the advice of a decorated military man in dealing with those officers could prove useful, so I invited him along.")
        character.speakADV("Actually, if it's not too much trouble, could you permit him to join me here? We didn't finish our review of the contracts before dinner, and I'd quite like to reach the end before we land.")
        Game.YOU.speakADV("Everyone is under suspicion, Mr. de la Rocque. Nobody leaves their cabins.")
        Game.narrateADV("(i)The gravity of the situation kills the momentary light in de la Rocque's eyes. He clears his throat and looks down at his shoes.(/i)")
        character.speakADV("Quite right, quite right. Yes, of course.")

        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Could he possibly have had anything against Mr. Royaume?")
            character.speakADV("Before this voyage, they'd never met, as far as I know. I handled all correspondence with him personally. Henry... didn't take much of an interest in the day-to-day.")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
label t_rook_pawn:
    python:
        character.speakADV("The steward? I understand from speaking with Captain Winfarthing she's been chronically away from her post during this voyage. Though some of that time she was waiting on the Royaumes. Henry never liked bringing his domestics along when travelling on his own vessels. Thought it was a frivolous expense. He paid the wages of these airmen, after all, he'd say.")
        
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Do you think she could have any connection to the murder?")
            Game.narrateADV("(i)de la Rocque nods gravely.(/i)")
            character.speakADV("We have to consider it. All these other so-called suspects are gentlemen, after all. I couldn't believe they would do such a thing. But her?")
        elif index == 1:
            pass
        Game.jump(character.label + "_loop")
label t_rook_queen:
    python:
        character.speakADV("Ah, the Lady Eleanora? Lovely woman, lovely woman. She was a perfect match for Henry. We'd never be where we are today if it weren't for her. Those royals can be such snobs. Even though we make ten times what they do in a year, they still turn up their noses at us. Eleanora gave Henry the respectability he needed to meet contacts in Her Infallible Majesty's government.")
       
        choices = ["Pressure", "Ask something else"]
        character.inputADV(Game.prevNarrate, choices)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Truly, a romance for the ages.")
            character.speakADV("How dare you, Detective!")
            Game.narrateADV("(i)de la Roque pauses, and the indignance fades from his face.(/i)")
            character.speakADV("Though, you are right. No one could accuse theirs of being a loving marriage. It was as political for her as it was for him; a lot of those old families are paying off generations worth of debts. And Henry - his personal fortune was quite large. Even though control of his company falls to me - I hate to think it, but Lady Eleanora could live out her days quite comfortably on her inheritance.")
        Game.jump(character.label + "_loop")
