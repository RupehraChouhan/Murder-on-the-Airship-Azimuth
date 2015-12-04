# Declare all images
image bg detectiveImage = "DetectiveSketch1.jpg"
image bg notepadImage = "NotepadSketch1.jpg"
image bg whiteImage = "#ffffff"
image bg blackImage = "#000000"

image bg map = "map.jpg"
image bg cabinImage = "PassengerCabinsSketch.jpg"
image bg diningImage = "DiningRoomSketch.jpg"
image bg galleyImage = "GalleySketch.jpg"
image bg bathImage = "BathsSketch.jpg"
image bg loungeImage = "PassengerLoungeSketch.jpg"
image bg barImage = "BarSketch.jpg"
image bg cargoHoldImage = "CargoHoldSketch.jpg"
image bg cockPitImage = "CockpitSketch.jpg"
image bg engineImage = "EngineRoomSketch.jpg"

image queen = "queen_clean.png"
image bishop = "bishop_clean.png"
image knight = "knight_clean.png"
image rook = "rook_clean.png"
image pawn = "pawn_clean.png"
image captain = "captain_clean.png"

image groupRook = "group_clean.png"
image groupNoRook = "group_without_rook_clean.png"

# The game starts here
label start:
    python:
        if not Game.introDone:
            Game.introDone = True
            Game.jump("intro")
            
    # background image for the main page 
    scene bg detectiveImage
    if Game.fadeStart:
        with fade
        $ Game.fadeStart = False
    
    # play music
    if Game.musicStart:
        play music Game.MUSIC_INTRO fadeout 2 fadein 2
        $ Game.musicStart = False
    
    # Player has taken too long, skip to ending sequence
    if Game.getMoves() >= 21:
        show captain
        $ Game.narrateADV("{i}Captain Winfarthing finds you.{/i}")
        $ Game.npcs[Game.NPC_CAPTAIN].speakADV("Detective, we're approaching the Endsville aerodrome. I have assembled the passengers in the lounge - guarded by all the airmen I could spare. Are you ready to identify the killer?")
        $ Game.YOU.speakADV("Of course, Captain! All will be revealed. Lead the way.")
        $ Game.jump("finale")
    
    python:
        prompt = "What would you like to do?\n"
        choices = ["Investigate a room", "Interview a suspect", "Check your findings", "Solve the case"]
        
        Game.inputNVL(prompt, choices)
        Game.checkQuit("start")
        
        try:
            option = int(Game.input) - 1
            
            if option == 0: Game.jump("investigate_room")
            if option == 1: Game.jump("talk_suspect")
            if option == 2: Game.jump("look_notepad")
            if option == 3: Game.jump("solve_case")
            
            # if no options are chosen
            Game.narrateNVL("I didn't understand \"[Game.input]\"")
        except ValueError:
            Game.narrateNVL("\"[Game.input]\" is not a number")
            
        # if we make it this far, the input was not understood
        Game.jump("start")

label investigate_room:
    $ Game.fadeStart = True
    scene bg map
   
    python:
        prompt = "The [Game.zeppelinName] has 9 rooms.\nWhich would you like to investigate?\n"
        choices = []
        for room in Game.rooms:
            choices.append(room.name);
        
        Game.inputNVL(prompt, choices)
        Game.checkQuit("investigate_room")

        # check for integer input
        try:
            index = int(Game.input) - 1
            Game.input = choices[index]
        except:
            # do nothing with error
            pass
        
        for r in Game.rooms:
            if r.match(Game.input) and r.label: # If matching, must have a label
                Game.incrementMoves() # Heading to a room counts as a move
                Game.jump(r.label)
        Game.narrateNVL("I don't know what room \"[Game.input]\" is.")
        Game.jump("investigate_room")

label talk_suspect:
    $ Game.fadeStart = True
    
    python:
        prompt = "Who would you like to talk to?\n"
        choices = []
        
        for npc in Game.npcs:
            if npc.alive:
                choices.append(npc.name)
        
        Game.inputNVL(prompt, choices)
        Game.checkQuit("talk_suspect")
        
        try:
            index = int(Game.input) - 1
            Game.input = choices[index]
        except:
            # do nothing with exceptions
            pass
        
        for n in Game.npcs:
            if n.match(Game.input) and n.label and n.alive: # If matching, must have a label and be alive
                Game.incrementMoves() # Talking to a suspect counts as a move
                Game.jump(n.label)
        Game.narrateNVL("I don't know who \"[Game.input]\" is.")
        Game.jump("talk_suspect")

label look_notepad:
    $ Game.fadeStart = True
    scene bg notepadImage
    
    python:
        startTime = Game.timeString(0)
        currentTime = Game.timeString(Game.getMoves())
        line = "Your watch reads [currentTime]. You started your investigation at [startTime]."
        
        for clueName, found in Game.cluesFound.items():
            if found:
                if clueName == Game.LOUNGE_CONTRACTS:
                    line += "\n\n{b}[Game.LOUNGE_CONTRACTS]{/b}: In the lounge you found a Royaume & Sons government contract, signed off by Mr. de la Rocque but not Mr. Royaume."
                elif clueName == Game.DINING_SPECTACLES:
                    line += "\n\n{b}[Game.DINING_SPECTACLES]{/b}: Rector Esgob's, found on a dining room table."
                elif clueName == Game.CARGO_RECORD:
                    line += "\n\n{b}[Game.CARGO_RECORD]{/b}: In the cargo hold you found Ritter's service record, detailing among other things his honourable discharge after the Battle of Rosenfeldt."
                elif clueName == Game.BATHS_WOUND:
                    line += "\n\n{b}[Game.BATHS_WOUND]{/b}: The murder was likely caused by a heavy metal object."
                elif clueName == Game.BATHS_TIME_OF_DEATH:
                    line += "\n\n{b}[Game.BATHS_TIME_OF_DEATH]{/b}: 20:42, from the broken pocket watch."
                elif clueName == Game.GALLEY_PIPE:
                    line += "\n\n{b}[Game.GALLEY_PIPE]{/b}: Hidden in a galley vent and wrapped in a bloody towel."
                elif clueName == Game.GALLEY_BOOK:
                    line += "\n\n{b}[Game.GALLEY_BOOK]{/b}: Book found in galley, infamous and revolutionary."
                elif clueName == Game.CABINS_EMPTY:
                    line += "\n\n{b}[Game.CABINS_EMPTY]{/b}: The murder weapon is not in the cabins."
                elif clueName == Game.ROOK_BODY:
                    line += "\n\n{b}[Game.ROOK_BODY]{/b}: The murderer has struck again. You found Mr. de la Rocque's body in the passenger cabins."
        
        Game.narrateADV(line)
        Game.jump("start")

label solve_case:
    $ Game.fadeStart = True
    
    python:
        Game.jump("finale")
