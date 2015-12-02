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
            Game.jump("finale_main")
        elif index == 2:
            Game.jump("finale_main")
        Game.jump("finale_main")
        
        
label finale_address_rook:
    python:
        Game.YOU.speakADV("Mr. de la Rocque.")
        rook.speakADV("Yes, what?")
        if Game.state[Game.CONV_ROOK_WHAT]:
            Game.YOU.speakADV("You claim you visited the cockpit following dinner?")
            rook.speakADV("Yes, but Captain Winfarthing was occupied navigating the storm.")
            Game.YOU.speakADV("So you returned to the passenger lounge to work on your contracts.")
            rook.speakADV("Yes, that's right. That would have been 8:30.")
            Game.YOU.speakADV("Then when the storm blew over at 9, you returned to the cockpit, spoke with the Captain, then returned to the dining room at 9:30?")
            rook.speakADV("That's correct.")
            Game.YOU.speakADV("Thank you.")
        
        if Game.state[Game.CONV_CAPTAIN_WHAT]:
            Game.YOU.speakADV("Captain, you said you saw Mr. de la Rocque at 9:00 last night?")
            captain.speakADV("Yes, we had a brief meeting.")
            Game.YOU.speakADV("You didn't see him before that?")
            captain.speakADV("No. My eyes were fixed to the instruments until we passed through that storm.")
        
        if Game.state[Game.CONV_BISHOP_WHAT]:
            Game.YOU.speakADV("Rector Esgob, you joined Mr. de la Rocque for coffee and cigars in the dining room at 9:30, yes?")
            bishop.speakADV("That's right.")
            
        if Game.cluesFound[Game.LOUNGE_CONTRACTS]:
            Game.YOU.speakADV("I found the draft copy of Royaume & Sons contract with the Admiralty in the passenger lounge. I have gathered that you, not Mr. Royaume, were principly responsible for the drafting of these contracts, so they were in your possession, not his. Since dinner was served immediately upon embarkment, this does place you in the lounge at some point after dinner.")
            rook.speakADV("I- I suppose so, yes.")
            Game.YOU.speakADV("That was not a question.")
            
        if Game.cluesFound[Game.GALLEY_PIPE] or Game.state[Game.STATE_ENGINE_MISSING_PIPE]:
            Game.YOU.speakADV("You are familiar enough with skyship engineering to know which pipes can be removed without causing a major disaster.")
            rook.speakADV("Yes, but why would I share that with you if I were the killer?")
            Game.YOU.speakADV("Precisely so you could ask me that question when we arrived at this point.")
            
        line = "Is he guilty?"
        choices = ["Guilty", "Innocent", "Potential"]
        Game.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.jump("finale_accuse_rook")
        elif index == 1:
            potentials[Game.NPC_ROOK] = False
            Game.jump("finale_main")
        elif index == 2:
            Game.jump("finale_main")
        Game.jump("finale_main")
        
        
label finale_address_bishop:
    python:
        Game.YOU.speakADV("Rector Nathaniel Esgob.")
        bishop.speakADV("V-very well, Detective.")
        
        if Game.state[Game.CONV_BISHOP_WHAT]:
            Game.YOU.speakADV("Rector Esgob, you claimed you were in your cabin after dinner, before returning to the dining room at 8:30?")
            bishop.speakADV("Yes.")
            if Game.state[Game.CONV_BISHOP_WHAT_PRESS]:
                Game.YOU.speakADV("But you were not in your cabin, were you? You were having a drink in the bar.")
                bishop.speakADV("I was rather hoping you'd keep that confidential.")
            Game.YOU.speakADV("Then you said you visited the bar at 9, before returning again to the dining room for coffee and cigars at 9:30?")
            bishop.speakADV("Yes, that's right.")
            
        if Game.state[Game.CONV_QUEEN_WHAT]:
            Game.YOU.speakADV("Lady Eleanora, you told me you saw Rector Esgob in the {i}bar{/i} at 8:30, yes?")
            queen.speakADV("Yes, though I'm not sure how many of {i}me{/i} he saw.")
            Game.narrateADV("{i}Esgob looks simultaneously incensed and sheepish, somehow.{/i}")
        
        if Game.state[Game.CONV_PAWN_WHAT_PRESS]:
            Game.YOU.speakADV("Miss Newport, you were with Rector Esgob from 9 until the coffee and cigars were served, yes?")
            pawn.speakADV("That's right.")
        
        if Game.state[Game.CONV_ROOK_WHAT]:
            Game.YOU.speakADV("And Mr. de la Roque, you joined the Rector for coffee and cigars at 9:30?")
            rook.speakADV("I did.")
            
        if Game.cluesFound[Game.DINING_SPECTACLES]:
            Game.YOU.speakADV("I discovered these in the dining room. They belong to you, yes?")
            bishop.speakADV("Y-yes. Yes they do.")
            Game.YOU.speakADV("All we can surmise from this discovery is that you were in the dining room at some point after supper.")
            
        line = "Is he guilty?"
        choices = ["Guilty", "Innocent", "Potential"]
        Game.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.jump("finale_accuse_bishop")
        elif index == 1:
            potentials[Game.NPC_BISHOP] = False
            Game.jump("finale_main")
        elif index == 2:
            Game.jump("finale_main")
        Game.jump("finale_main")

label finale_address_knight:
    python:
        Game.YOU.speakADV("Sergeant-Major Ritter.")
        Game.narrateADV("{i}Ritter nods brusquely{/i}")
        knight.speakADV("Detective.")
        
        if Game.state[Game.CONV_KNIGHT_WHAT]:
            Game.YOU.speakADV("Sergeant-Major, you claimed you went to the cargo hold after dinner and were back in your cabin by 8:30. You remained there until 9:30 where you visited the observation deck near the cockpit.")
            knight.speakADV("That is correct.")
        
        if Game.state[Game.CONV_QUEEN_WHAT]:
            Game.YOU.speakADV("And nobody saw you at all between dinner and 9:30, when you encountered Lady Eleanora on the observation deck?")
            queen.speakADV("Yes, that's correct.")
        
        line = "Is he guilty?"
        choices = ["Guilty", "Innocent", "Potential"]
        Game.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.jump("finale_accuse_knight")
        elif index == 1:
            potentials[Game.NPC_KNIGHT] = False
            Game.jump("finale_main")
        elif index == 2:
            Game.jump("finale_main")
        Game.jump("finale_main")
    
label finale_address_pawn:
    python:
        Game.YOU.speakADV("Steward Polly Newport.")
        pawn.speakADV("Uhh, yes?")
        
        if Game.state[Game.CONV_PAWN_WHAT]:
            Game.YOU.speakADV("Miss Newport, you claim you saw the guests off after dinner, and then waited on Mr. Royaume in the lounge until you slipped away at 8:30, is that right?")
            pawn.speakADV("Yes it is.")
            Game.YOU.speakADV("Whereupon you resumed your duties. You assisted in the cockpit until the storm blew over at 9, then tidied the bar until 9:30, when you made the rounds of the vessel to inform the passengers that coffee and cigars were to be served. You began with the baths, which is where you found Mr. Royaume's body, correct?")
            pawn.speakADV("Yes, that's all right.")
        
        if Game.state[Game.CONV_BISHOP_WHAT]:
            Game.YOU.speakADV("Rector Esgob, you can confirm that Miss Newport was in the bar from nine o'clock until half-past?")
            bishop.speakADV("I-I think so. That sounds right, yes.")
            
        if Game.cluesFound[Game.GALLEY_BOOK]:
            Game.YOU.speakADV("I discovered this book of yours in the galley. Now, if you are to be believed, you have been run off your feet by the extra demands of Mr. Royaume ever since he boarded, not leaving you any time to attend to your duties in the galley. However, as a member of the crew, you could easily have left it there before we passengers embarked.")
            pawn.speakADV("That - that's what happened.")
            
        if Game.cluesFound[Game.GALLEY_PIPE]:
            Game.YOU.speakADV("Furthermore, you are familiar enough with this ship to know where to conceal a large, incriminating weapon.")
            pawn.speakADV("But... I never... Why would I tell you about it, then?")
            Game.YOU.speakADV("Precisely so you could ask me that question. But I have not finished yet.")
            
        line = "Is she guilty?"
        choices = ["Guilty", "Innocent", "Potential"]
        Game.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.jump("finale_accuse_pawn")
        elif index == 1:
            potentials[Game.NPC_PAWN] = False
            Game.jump("finale_main")
        elif index == 2:
            Game.jump("finale_main")
        Game.jump("finale_main")
        
label finale_accuse_queen:
    python:
        Game.YOU.speakADV("For these reasons, I have no choice but to accuse you, Lady Eleanora Francesca van Koenigen Royaume, for the murder of your husband, Henry Augustus Algernon Royaume. ")
        line = "What? That's outrageous! What possible reason could I have for killing him?"
        queen.speakADV(line)
        
        choices = ["Money", "A lover", "Resentment"]
        queen.inputADV(line, choices, True)
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
    python:
        Game.YOU.speakADV("For these reasons, I have no choice but to accuse you, Sergeant-Major Angus Ritter, for the murder of Henry Augustus Algernon Royaume.")
        Game.narrateADV("{i}Ritter doesn't even flinch.{/i}")
        
        line = "That's absurd. What could possibly be my motive? I'd never even met the man before tonight."
        knight.speakADV(line)
        
        choices = ["Money", "Revenge", "Principles"]
        if Game.cluesFound[Game.CARGO_RECORD]:
            choices.append("Saving Lives")
        knight.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("You stand to profit from his death.")
            knight.speakADV("No, I - what?")
            Game.YOU.speakADV("Yes, after your regiment's losses at Rosenfeldt, you developed a long-term interest in the safe and responsible use of zeppelins in war. Retiring at your age on a Sergeant-Major's pension - even decorated as you are - does not lead to a life of much comfort.")
            knight.speakADV("I don't know what you're talking about.")
            Game.YOU.speakADV("You recently took out a loan to purchase your own zeppelin manufactorium!")
            knight.speakADV("This is... pure fiction.")
            Game.YOU.speakADV("But then Royaume's exclusive government contracts made headlines! There was no way to compete with an enterprise of that scale, so you killed him in an effort to kill the deal!")
            knight.speakADV("What nonsense.")
            Game.YOU.speakADV("Captain, take him to the brig!")
            captain.speakADV("You have been a litte light on offering proof, Detective. Have you any evidence that proves Ritter was in the zeppelin trade?")
            Game.YOU.speakADV("No, but I'm certain they exist.")
            captain.speakADV("I'm... not. I'm afraid I must confine all of you to your berths and let the Metropolitan Police sort this out.")
            Game.narrateADV("{i}Captain Winfarthing looks you straight in the eyes.{/i}")
            captain.speakADV("I apologize for placing my trust in this so-called detective.")
            
            Game.jump("finale_no_arrest")
            
        elif index == 1:
            Game.YOU.speakADV("Revenge.")
            knight.speakADV("Revenge? I just said we'd never met!")
            Game.YOU.speakADV("Yes, but you'd met his handiwork. On the battlefield, Royaume ships have caused the deaths of many of your comrades. More men died at Rosenfeldt to crashing Royaume zeppelins than to the guns of the enemy.")
            knight.speakADV("You hardly need to remind me of that. But that was years ago. Why act now?")
            Game.YOU.speakADV("You saw Royaume's name in the paper and contacted his firm. You made yourself useful to get close to him, then you murdered him for a years-old grudge.")
            Game.YOU.speakADV("Captain! Take him to the brig!")
            captain.speakADV("Very well. Guards!")
            Game.narrateADV("{i}Ritter fixes you with a level stare.{/i}")
            knight.speakADV("That may be true, Detective. Maybe I did hate the man. But I hated what he was going to do more. Can you imagine? Dozens of Rosenfeldts on battlefields all around Her Infallible Majesty's Dominions? I was saving lives, Detective!")
            Game.narrateADV("{i}Ritter fixes de la Rocque with a hateful glare.{/i}")
            knight.speakADV("You'd have been next if I'd had the time! You're the murderer, not me! Tear up that contract! You're dooming the soldiers who fight for your queen to die in flames!")
            Game.narrateADV("{i}Ritter's shouts echo down the corridor as the airmen drag him below.{/i}")
                        
            Game.jump("finale_correct")
            
        elif index == 2:
            Game.YOU.speakADV("You are ideologically opposed to the use of modern technology in warfare. You saw Royaume's war zeppelin contract as an affront to the dignity of the common foot soldier.")
            knight.speakADV("An interesting suggestion. How do you intend to prove it?")
            Game.YOU.speakADV("I suppose I can't at this time.")
            knight.speakADV("Then you really going to have me arrested based on that supposition?")
            Game.narrateADV("{i}The Sergeant-Major stands up and places his wrists together in front of him.{/i}")
            knight.speakADV("Captain, if it would make the voyage more secure, I will remand myself to your custody. But I suggest you keep guard on the others as well. This so-called detective has wasted time imagining things about me while a killer stalks the ship.")
            
            Game.jump("finale_no_arrest")
            
        elif index == 3:
            Game.YOU.speakADV("You murdered him because you believed you were saving lives.")
            bishop.speakADV("What do you mean by that?")
            knight.speakADV("Yes, Detective, explain yourself.")
            Game.YOU.speakADV("Your medals come from your heroics at the Battle of Rosenfeldt, the historic first deployment of Her Majesty's Imperial Aeronautic Squadrons - the war zeppelins.")
            knight.speakADV("That's hardly unique.")
            Game.YOU.speakADV("The war zeppelins were a disaster. Their bombing runs traversed our own lines, killing many of Her Infallible Majesty's brave soldiers. When the lightly-armoured, flammable vessels were shot down, they killed many more.")
            knight.speakADV("You hardly need to remind me.")
            Game.YOU.speakADV("If Royaume's deal goes through, dozens more war zeppelins will be commissioned, leading, in your mind, to dozens more disasters like the one at Rosenfeldt.")
            Game.YOU.speakADV("You thought killing Royaume would save the lives of hundreds of enlisted men, so you contacted his company and made yourself useful so you could get close to him.")
            Game.YOU.speakADV("Captain! Take him to the brig!")
            Game.narrateADV("{i}Ritter fixes his eyes to yours in a level stare until the captain's airmen haul him away.")
            
            Game.jump("finale_correct")
label finale_accuse_rook:
    python:
        Game.YOU.speakADV("For these reasons, I have no choice but to accuse you, Mr. Charles Westinghouse de la Rocque, for the murder of your client and business partner, Henry Augustus Algernon Royaume.")
        
        line = "What? That's outrageous! What possible reason could I have for killing him?"
        rook.speakADV(line)
        
        choices = ["Money", "Resentment", "A lover"]
        rook.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("The death of your business parter enriches you greatly, sir. You were already the brains behind Royaume & Sons, and without Royaume's impulsiveness causing you trouble, you figured your shrewd mind could further grow your firm's profits - without a partner to split them with, no less. But you didn't gamble on encountering a yet-shrewder mind, eh?")
            Game.YOU.speakADV("Captain, take him to the brig!")
            rook.speakADV("What? This is preposertous! It wasn't me! All that's true, yes, but I didn't kill him! I'm being set up! You have to believe me!")
            Game.jump("finale_incorrect")
            
        elif index == 1:
            Game.YOU.speakADV("You were constantly living in Royaume's shadow. You did all the work, while he got all the credit. His name on the company! His name in the papers! His marriage to an aristocratic bride! All thanks to your tireless efforts! With him dead, and you on your way to the most lucrative business deal of your career, it would be {i}you{/i} who finally gets the recognition you deserve! {i}You{/i} whose name is signed just below the seal of Her Infallible Majesty's Grand Admiral!")
            Game.YOU.speakADV("Well, you'll get your wish. You'll have your name in the papers. But not, I think, in the manner you desired. Captain! Take him to the brig!")
            Game.jump("finale_incorrect")
            
        elif index == 2:
            Game.YOU.speakADV("You were overcome with jealousy.")
            rook.speakADV("What?")
            Game.YOU.speakADV("Over a woman!")
            rook.speakADV("What?!")
            Game.YOU.speakADV("{i}That{/i} woman!")
            queen.speakADV("WHAT?!")
            Game.YOU.speakADV("With Royaume dead, you were free to romance his widow! Assuming you weren't already!")
            Game.narrateADV("{i}de la Rocque and Lady Eleanora give each other sidelong glances. They stifle laughter.{/i}")
            rook.speakADV("Romance {i}her{/i}?")
            queen.speakADV("Romance {i}him{/i}?")
            rook.speakADV("Captain, this is a farce. Have you any proof, Detective?")
            Game.YOU.speakADV("A detective simply knows, sir.")
            rook.speakADV("This is outrageous! Lock this so-called \"detective\" up.")
            Game.YOU.speakADV("Captain! Take him to the brig!")
            captain.speakADV("I'm inclined to side with the gentleman, Detective. Without proof, I'm afraid I must confine all of you to your berths and let the Metropolitan Police sort this out.")
            Game.narrateADV("{i}Captain Winfarthing looks you straight in the eyes.{/i}")
            captain.speakADV("I apologize for placing my trust in this so-called detective.")
            Game.jump("finale_no_arrest")
            
label finale_accuse_bishop:
    python:
        Game.YOU.speakADV("For these reasons, I have no choice but to accuse you, Rector Nathaniel Esgob, for the murder of Henry Augustus Algernon Royaume.")
        
        line = "What? That's outrageous! What possible reason could I have for killing him?"
        bishop.speakADV(line)
        
        bishop.inputADV(line, choices, True)
        choices = ["On request", "Passion", "Politics"]
        bishop.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("You murdered Royaume as directed by another! Your motives were purely mercenary.")
            bishop.speakADV("That's ridiculous! Who could have put me up to it?")
            Game.YOU.speakADV("None other than Lady Eleanora Francesca van Koenigen Royaume!")
            queen.speakADV("What?")
            Game.YOU.speakADV("I don't know what she offered you - money, public support for your positions, the cessation of child labour in Royaume factories - but she offered you enough incentive and enough brandy that you accepted.")
            bishop.speakADV("This is most absurd.")
            queen.speakADV("I don't have to listen to this.")
            Game.YOU.speakADV("We'll deal with you momentarily!")
            Game.YOU.speakADV("Captain, take them both to the brig!")
            captain.speakADV("This has gotten too confusing to follow. I'm afraid I must confine all of you to your berths and let the Metropolitan Police sort this out.")
            Game.narrateADV("{i}Captain Winfarthing looks you straight in the eyes.{/i}")
            captain.speakADV("I apologize for placing my trust in this so-called detective.")
            
            Game.jump("finale_no_arrest")
                    
        elif index == 1:
            Game.YOU.speakADV("A simple crime of passion. You'd had plenty to drink, Rector. You'd argued. The man was, by all accounts, a dreadful boor.")
            Game.narrateADV("{i}Lady Eleanora nods silently.{/i}")
            Game.YOU.speakADV("Here you are, thinking you've finally gained some traction for your views among the great and powerful. It turns out, they all look down on you. And this lout has the courage to say so.")
            Game.YOU.speakADV("You drink more. You see red. You find a bludgeon. You crush his skull.")
            Game.YOU.speakADV("Captain! Take him to the brig!")
            
            Game.jump("finale_incorrect")
            
        elif index == 2:
            Game.YOU.speakADV("One dinner with an industrial magnate was all it took to realize that your views will never find traction among those with the power to make a difference. At least, not with Mr. Royaume. You figured that the more even-tempered Mr. de la Rocque might be more agreeable, so you... hastened the transition.")
            Game.YOU.speakADV("Captain! Take him to the brig!")
            bishop.speakADV("No, you can't! It wasn't me! All that's true, yes, but I didn't kill him! I'm being set up! You have to believe me!")
                    
            Game.jump("finale_incorrect")
            
label finale_accuse_pawn:
    python:
        Game.YOU.speakADV("For these reasons, I have no choice but to accuse you, Miss Polly Newport, for the murder of your employer, Henry Augustus Algernon Royaume.")
        pawn.speakADV("What? I never did! This is just so you don't have to go to the trouble of arresting someone with money or power!")
        line = "Not at all. I'll tell you why I'm accusing you."
        Game.YOU.speakADV(line)
        
        choices = ["Politics", "Revenge", "Resentment"]
        Game.YOU.inputADV(line, choices, True)
        index = int(Game.input) - 1
        if index == 0:
            Game.YOU.speakADV("Based on your choice in literature, you have Singerist sympathies. You believe in the violent overthrow of the bourgeois industrialist class. Why not start with the most bourgeois industrialist of all, Henry Augustus Algernon Royaume?")
            pawn.speakADV("I don't {i}believe{/i} all that stuff, not the violent bits! I just go to some meetings with friends is all!")
            Game.YOU.speakADV("What better way to impress those friends than with a daring act in line with their politics?")
            Game.narrateADV("{i}The assembled passengers nod gravely.{/i}")
            Game.YOU.speakADV("Captain, take her to the brig!")
            pawn.speakADV("No, you can't! It wasn't me!")
            Game.narrateADV("{i}Newport's face twists into a grimace.{/i}")
            pawn.speakADV("You rich parasites! You think you can just treat us like dirt! Well, I didn't kill him, but I wish I did! But that doesn't matter to you, does it? It's not about justice. It's about oppression. Well, the revolution is coming, and you'll all be the first batch on the chopping block! I'll tell my story!")
            
            Game.jump("finale_incorrect")
            
        elif index == 1:
            Game.YOU.speakADV("You sought revenge against Mr. Royaume, who was...")
            Game.YOU.speakADV("Your unacknowledged father!")
            pawn.speakADV("What?")
            Game.YOU.speakADV("Yes, you're his illegitimate daughter. He arranged to have you hired on at his company because he couldn't bear the thought of you living in squalour, but he couldn't acknowledge you, now that he moves in aristocratic circles. Seeing him here with his wife was too much for you.")
            Game.YOU.speakADV("Captain! Take her to the brig!")
            pawn.speakADV("What nonsense are you spouting? My parents are Peter and Nora Newport. They've lived in Edelwich Crossing their whole lives. I doubt Mr. Royaume's ever {i}been{/i} to Edelwich Crossing. Unless... can you prove it?")
            Game.YOU.speakADV("A detective simply knows, Miss Newport.")
            captain.speakADV("I'm inclined to side with my steward, Detective. Without proof, I'm afraid I must confine all of you to your berths and let the Metropolitan Police sort this out.")
            Game.narrateADV("{i}Captain Winfarthing looks you straight in the eyes.{/i}")
            captain.speakADV("I apologize for placing my trust in this so-called detective.")
            
            Game.jump("finale_no_arrest")
            
        elif index == 2:
            Game.YOU.speakADV("Your resentment of Mr. Royaume's demands for extra attention became too much. He'd travelled on your ship before. You knew you would end up being disciplined just because the man couldn't fetch his own nightcaps or be bothered to bring his butler along.")
            Game.YOU.speakADV("After dinner, you of course had duties to attend to. There were dishes to clean, a bar to tidy, and storm damage to repair. And you knew none of that would get done if Royaume monopolized your time like he always did. You didn't want to lose your job, so you made sure Royaume could make no more demands on your time. I'm afraid you'll lose more than just your job for that decision, Miss Newport.")
            Game.YOU.speakADV("Captain! Take her to the brig!")
            pawn.speakADV("No, you can't! It wasn't me! Do you believe this, Captain?")
            Game.narrateADV("{i}Newport's face twists into a grimace.{/i}")
            pawn.speakADV("You rich parasites. You don't care about justice, do you? You just want things tidied away, don't want to admit that it might be one of your own! That having money or an old name doesn't make you better than everyone else!")
                    
            Game.jump("finale_incorrect")
        
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
        
label finale_correct:
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