# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label t_captain:
    stop music fadeout 2
    python:
        # character you are talking to
        character = Game.npcs[Game.NPC_CAPTAIN]
        
        # NPC speaks
        Game.prevNarrate = "What do you want me to say"
        Game.jump(character.label + "_loop")
        
label t_captain_loop:
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
        
label t_captain_you:
    python:
        character.speakADV("I'm the skipper of the {i}Azimuth{/i}. Sixteen years before the gasbag.")
        Game.jump(character.label + "_loop")

label t_captain_vic:
    python:
        character.speakADV("He built this ship and owns the line, so he does pay my wages. That said, since I welcomed him and his party on board, we haven't spoken. I and my crew have been busy non-stop keeping us aloft. Except for my steward, Miss Newport - she's been away from her post a fair bit lately.")
        Game.jump(character.label + "_loop")

label t_captain_saw:
    python:
        character.speakADV("We flew through a stormcloud, so I didn't leave the wheel from half-past-seven until almost nine. It's all there in my logbook, and my crew can attest to that. If anyone came through the observation deck during that time, I wouldn't have noticed. After it blew over, I had a word with Mr. de la Rocque. Routine scheduling and maintenance discussion. I glanced up after 9:30 and saw Lady Eleanora and Sergeant-Major Ritter taking in the view.")
        Game.jump(character.label + "_loop")

label t_captain_found:
    python:
        line = "Ask about what?"
        choices = []

        for clueName, found in Game.cluesFound.items():
            if found:
                choices.append(clueName)
        choices.append("Ask something else")

        Game.inputADV(line, choices, True)

        index = int(Game.input) - 1
        clueName = choices[index]

        if clueName == Game.BATHS_WOUND:
                character.speakADV("I run a tight ship. Nothing big and heavy should have been accessible to the passengers unless they smuggled it in under their clothes. If they went out-of-bounds, they might have found something in the engine room or the cargo bay.")

        elif clueName == Game.BATHS_TIME_OF_DEATH:
            character.speakADV("Between 8:30 and 9 we were still in the grips of that storm. I was stuck to the wheel. If anyone came through, I wouldn't have noticed until the storm passed.")

        elif clueName == Game.GALLEY_PIPE:
            character.speakADV("Ah, blast it. The responsonomic baro-regulator. Should have known. Let's get that reattached before we lose boiler pressure.")

        elif clueName == Game.CABINS_EMPTY:
            character.speakADV("I've had my men search all the usual contraband stashes. Nothing. Means there's one out there I don't know about. It {i}didn't{/i} go over the side, I can be sure of that. My instruments would have told me if we lost interior pressure. No worries there.")

        elif clueName == Game.DINING_SPECTACLES:
            character.speakADV("I'm not sure what you want me to say about those.")

        elif clueName == Game.LOUNGE_CONTRACTS:
            character.speakADV("Looks like de la Rocque handled most of the minutiae here. Not surprised. He always takes an interest in the day-to-day when he travels with us.")

        elif clueName == Game.GALLEY_BOOK:
            character.speakADV("Whose is this? Did anyone see you find this? If management hears we've got Singerist propaganda on board, lots of good airmen could lose their jobs.")

        elif clueName == Game.CARGO_RECORD:
            character.speakADV("Well, I knew he was a big hero, but I never knew exactly for what. Now I know why he doesn't go around boasting. No one wants to boast about Rosenfeldt.")
            Game.YOU.speakADV("Rosenfeldt?")
            character.speakADV("The first use of skyships in war. Three boats much like this one, minus all the mahogany.")
            Game.narrateADV("{i}Captain Winfarthing shakes her head solemnly.{/i}")
            character.speakADV("They crewed them with raw recruits out of the naval college. The {i}naval{/i} college. They weren't aeronauts. They didn't have a prayer.")
            character.speakADV("Got caught by some crosswinds, lost their position, ended up dropping their bombs on a regiment of Her Infallible Majesty's crack infantry. Then, when the Rurovians turned their guns on them...")
            character.speakADV("They {i}became{/i} the bombs.")
            Game.narrateADV("{i}Captain Winfarthing shudders.{/i}")
            character.speakADV("Anyone surviving Rosenfeldt got sent home with medals. I doubt it's enough.")

        elif clueName == Game.ROOK_BODY:
            character.speakADV("A damn shame. I've asked my men. No one heard anything. I don't have enough people to watch these people and fly the ship! Blast it!")
            character.speakADV("... I'm sorry, Detective. I know you're doing your best. But please hurry. With the murderer on the loose, we're all in danger.")

        elif clueName == "Ask something else":
            pass
        else:
            character.speakADV("I don't know what you're talking about.")        
        Game.jump(character.label + "_loop")

label t_captain_other:
    python:
        character.speakADV("Given the prestige of our passengers, I've had the... pleasure of speaking with them personally.")
        character.speakADV("As for Royaume, the, ah, victim, I don't know anything more than what you read in the papers. He owns this ship, he owns the whole airship line. He was headed to Endsville to sign the biggest contract Her Infallible Majesty's government has ever offered, selling war zeppelins to the Brigades.")
        character.speakADV("His wife, Baroness Eleanora is on board as well. Things are chilly between them, but if you keep up with the society pages, you'll know that's nothing new.")
        character.speakADV("Travelling with them is Mr. de la Rocque who is - was - Royaume's solicitor and business partner. We also have Colonel Angus Ritter, the war hero, and Rector Nathaniel Esgob, the social reformer. I understand he's on a speaking tour.")
        character.speakADV("Finally, though I hate to think it, one of my crew was not accounted for early this evening. My steward, Newport, was not at her post last night. I've taken the liberty of confining her to the passenger quarters with the other suspects. I hope you can resolve this swiftly and discreetly.")