label finale:
    python:
        queen = Game.npcs[Game.NPC_QUEEN]
        knight = Game.npcs[Game.NPC_KNIGHT]
        rook = Game.npcs[Game.NPC_ROOK]
        pawn = Game.npcs[Game.NPC_PAWN]
        bishop = Game.npcs[Game.NPC_BISHOP]
        captain = Game.npcs[Game.NPC_CAPTAIN]
        
        potentials = {Game.NPC_QUEEN:True, Game.NPC_KNIGHT:True, Game.NPC_BISHOP:True, Game.NPC_ROOK:True, Game.NPC_PAWN:True}
        
        # prelude, characters talking, you talking
        # establish the facts
        # weapon
        # weapon location
        # nobody was together at the time of the murder
        Game.YOU.speakADV("I have examined the evidence and spoken with the suspects, and I am prepared to reveal the identity of the killer. Captain, have your men on hand to apprehend the scoundrel.")
        if Game.cluesFound[Game.BATHS_TIME_OF_DEATH] or Game.cluesFound[Game.GALLEY_PIPE] or Game.state[Game.STATE_ENGINE_MISSING_PIPE]:
            Game.YOU.speakADV("The facts are these:")
            if Game.cluesFound[Game.BATHS_TIME_OF_DEATH]:
                Game.YOU.speakADV("From Mr. Royaume's shattered watch - the detective's best friend - we know that he was murdered between 8:30 and 9 PM. IF we can determine who was unaccounted for at that time, we narrow our list of suspects.")
            if Game.cluesFound[Game.GALLEY_PIPE]:
                Game.YOU.speakADV("The weapon - a length of pipe - was recovered from a hidden nook in the galley. IF we can determine who could have visited the galley unobserved after the murder took place, we can narrow the list of suspects further.")
            if Game.state[Game.STATE_ENGINE_MISSING_PIPE]:
                Game.YOU.speakADV("The weapon was obtained from a machine in the engine room. Since none of you was smeared with soot at dinner, we can surmise that the killer retrieved the weapon after dinner, between 8 and 8:30. We can limit our list of suspects to those who weren't accounted for at those times.")
            Game.YOU.speakADV("Do you accept these premises? They are perfectly logical, yes? Good.")
        
        Game.YOU.speakADV("Now, I will address each of you in turn, determine your whereabouts from your statements, the statements of your fellow passengers, and the physical evidence of your passage. Let us begin.")
        Game.jump("finale_main")

label finale_main:
    python:
        # address each in turn and evaluate motives and opportunity
        line = "Who do would you like to talk about?"
        choices = []
        labels = []
        for i in range(0, len(Game.npcs)):
            if i in potentials and potentials[i]:
                choices.append(Game.npcs[i].name)
                labels.append(Game.npcs[i].label)
    
        Game.inputADV(line, choices, True)
        index = int(Game.input) - 1
        label = labels[index]
        Game.jump("finale_address_" + label)
        
label finale_address_queen:
    python:
        # address QUEEN
        Game.YOU.speakADV("Lady Eleanora.")
        queen.speakADV("Proceed, Detective. I've nothing to hide.")
        
        # mention - relationship, large inheritance, whereabouts, what people said
        # reject, keep, accuse
        if Game.state[Game.CONV_QUEEN_WHAT]:
            Game.YOU.speakADV("Lady Eleanora, you said you visited the bar after dinner, before moving to the galley, then lounge, then cockpit, is that correct?")
            queen.speakADV("Yes, it is.")
        if Game.state[Game.CONV_KNIGHT_WHAT]:
            Game.YOU.speakADV("Sergeant-Major, you said you encountered Lady Eleanora on the observation deck just before Miss Newport discovered the body?")
            knight.speakADV("That's correct.")
            Game.YOU.speakADV("That would be around 9:30, yes?")
            knight("Correct.")
        if Game.state[Game.CONV_BISHOP_WHAT_PRESS]:
            Game.YOU.speakADV("Rector Esgob, you joined Lady Eleanora for a drink after dinner.")
            Game.narrateADV("{i}Esgob looks ashamed, but mumbles assent.{/i}")
            bishop.speakADV("That's right.")
            Game.YOU.speakADV("From the conclusion of dinner at eight o'clock for about half an hour, yes?")
            bishop.speakADV("That's correct.")
            
            
        line = "Is she guilty?"
        choices = ["Guilty", "Innocent", "Potential"]
        Game.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.jump("finale_accuse_queen")
        elif index == 1:
            potentials[Game.NPC_QUEEN] = False
        elif index == 2:
            pass
        Game.jump("finale_main")
        
        
label finale_address_rook:
    python:
        # address ROOK
        pass
        
label finale_address_bishop:

label finale_address_knight:

label finale_address_pawn:

label finale_accuse_queen:
    python:
        Game.YOU.speakADV("For these reasons, I have no choice but to accuse you, Lady Eleanora Francesca van Koenigen Royaume, for the murder of your husband, Henry Augustus Algernon Royaume. ")
        line = "What? That's outrageous! What possible reason could I have for killing him?"
        queen.speakADV(line)
        
        choices = ["Money", "A lover", "Resentment"]
        Game.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("The death of your husband enriches you greatly, Madame. It restores the fortunes of your fading aristocratic family - something which you place a great deal of value in. Henceforth, the van Koenigens will find themselves with wealth to match their station. That is, until this scandal makes the newspapers.")
            Game.YOU.speakADV("Captain, take her to the brig!")
            queen.speakADV("No, you can't! It wasn't me! All that's true, yes, but I didn't kill him! I'm being set up! You have to believe me!")
            Game.jump("finale_incorrect")
            
        elif index == 1:
            Game.YOU.speakADV("You have a secret lover, Madame. One who you favour far more than the husband fate had saddled you with. With Mr. Royaume out of the way, you can marry your true beloved. His name I do not know, but I know he is waiting for you in Endsville! Instead, the Metropolitan Police will be your rendez-vous, Madame. ")
            Game.YOU.speakADV("Captain! Take her to the brig!")
            queen.speakADV("That's absurd! What evidence do you have that such a man exists?")
            Game.YOU.speakADV("A detective simply knows, Madame.")
            captain.speakADV("I'm inclined to side with the Baroness, Detective. Without proof, I'm afraid I must confine all of you to your berths and let the Metropolitan Police sort this out.")
            Game.narrateADV("{i}Captain Winfarthing looks you straight in the eyes.{/i}")
            captain.speakADV("I apologize for placing my trust in this so-called detective.")
            Game.jump("finale_no_arrest")
            
        elif index == 2:
            Game.YOU.speakADV("You were overcome with frustration at your boorish bourgeois husband. His indecorous behaviour at dinner was the last straw. You killed him, fuelled by aristocratic ardour. Well, I hope your quality table manners serve you well in prison! ")
            Game.YOU.speakADV("Captain! Take her to the brig!")
            queen.speakADV("No, you can't! It wasn't me! All that's true, yes, but I didn't kill him! I'm being set up! You have to believe me!")
            Game.jump("finale_incorrect")
        
        
label finale_accuse_knight:

label finale_accuse_rook:

label finale_accuse_bishop:

label finale_accuse_pawn:

label finale_incorrect:
    python:
        Game.narrateADV("{i}A satisfied smile spreads across your face as an airman escorts the accused away. The rest of the passengers look on you with awe and admiration.{/i}")
        captain.speakADV("Detective... what can I say. Thank you. Your reputation is well-deserved.")
        Game.narrateADV("{i}The mood of the rest of the voyage is uneventful. Soon enough, the Azimuth docks with the aerodrome in Endsville.{/i}")
        Game.narrateADV("{i}As promised, the Metropolitan Police are on hand. You explain the details of the case and your brilliant deductions to the inspector while Captain Winfarthing's burliest airmen transfer custody of the accused to the constables.{/i}")
        Game.narrateADV("{i}As promised, the Metropolitan Police are on hand. You explain the details of the case and your brilliant deductions to the inspector while Captain Winfarthing's burliest airmen transfer custody of the accused to the constables.{/i}")
        Game.narrateADV("{i}The inspector thanks you, all the passengers and crew thank you again, and you spare a few words for the newspaper reporters that hang around the aftermath of these sorts of thing.{/i}")
        Game.narrateADV("{i}With the adoring public satisfied, you engage a hansom to take you and your bags to your hotel, where you manage to finally get back to sleep.{/i}")
        Game.narrateADV("{i}A few days into your vacation (a self-guided walking tour of Endsville's historic Watchmaker's District), you read a troubling headline.{/i}")
        Game.narrateADV("'WAR HERO FOUND DEAD, ADMITS TO MURDERS'")
        Game.narrateADV("{i}Apparently, Sergeant-Major Ritter, unable to clear the guilt of murder from his conscience, took his own life.{/i}")
        Game.narrateADV("{i}What bothers you more, though, is the drop head underneath the main headline.{/i}")
        Game.narrateADV("'GREAT DETECTIVE GETS IT WRONG -- DOZENS OF CASES CALLED INTO QUESTION'")
        
        Game.jump("the_end")
        
label correct:
    python:
        Game.narrateADV("{i}A satisfied smile spreads across your face as an airman escorts Ritter away. The rest of the passengers look on you with awe and admiration.{/i}")
        captain.speakADV("Detective... what can I say. Thank you. Your reputation is well-deserved.")
        Game.narrateADV("{i}The mood of the rest of the voyage is uneventful. Soon enough, the Azimuth docks with the aerodrome in Endsville.{/i}")
        Game.narrateADV("{i}As promised, the Metropolitan Police are on hand. You explain the details of the case and your brilliant deductions to the inspector while Captain Winfarthing's burliest airmen transfer custody of the sergeant-major to the constables.{/i}")
        Game.narrateADV("{i}The inspector thanks you, all the passengers and crew thank you again, and you spare a few words for the newspaper reporters that hang around the aftermath of these sorts of thing.{/i}")
        Game.narrateADV("{i}With the adoring public satisfied, you engage a hansom to take you and your bags to your hotel, where you finally manage get back to sleep.{/i}")
        
        Game.jump("the_end")
        
label finale_no_arrest:
    python:
        Game.narrateADV("{i}The rest of the voyage passes with the passengers - yourself included - under guard, while the ship sails with a skeleton crew.{/i}")
        Game.narrateADV("{i}Upon arriving in Endsville, all of the passengers - again, yourself included - spend a long time being questioned by inspectors of the Metropolitan Police.{/i}")
        Game.narrateADV("{i}They are as unconvinced by your deductions as Captain Winfarthing was.{/i}")
        Game.narrateADV("{i}Eventually, you are released, but your vacation is ruined - especially when you see the headline in the morning paper.{/i}")
        Game.narrateADV("MURDER ON THE SKYSHIP {i}AZIMUTH!{/i} - GREAT DETECTIVE BAFFLED!")
        Game.narrateADV("Your good name, your reputation for brilliance, all gone in an instant.")
        
        Game.jump("the_end")
        
label the_end: