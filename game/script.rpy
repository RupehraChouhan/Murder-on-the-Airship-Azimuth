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
    
    python:
            
        prompt = "What would you like to do?\n"
        choices = ["Investigate a room", "Talk to a passenger", "Look at your pocketwatch", "Solve the case"]
        
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
        moves = Game.getMoves()
        time = Game.timeString()
        line = "Your watch reads [time]."
        if Game.cluesFound[Game.BATHS_TIME_OF_DEATH]:
            line += " You know the murder happened at 8:42."
        else:
            line += " The murder happened somewhere between 8:30 and 9:00."
            
        Game.narrateADV("Your watch reads [time].")
        Game.jump("start")

label solve_case:
    $ Game.fadeStart = True
    
    python:
        Game.jump("finale")
