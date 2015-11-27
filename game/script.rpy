# The game starts here

image bg detectiveImage = "DetectiveSketch1.jpg"
image bg barImage  = "BarSketch1.jpg"
image bg bathImage = "BathSketch2.jpg"
image bg cargoHoldImage = "CargoHoldSketch1.jpg"
image bg cockPitImage = "CockPitSketch2.jpg"
image bg diningImage = "DiningSketch1.jpg"
image bg engineImage = "EngineSketch1.jpg"
image bg galleyImage = "GalleySketch1.jpg"
image bg notepadImage = "NotepadSketch1.jpg"
image bg cabinImage = "PassengerCabinSketch1.jpg"
image bg loungeImage = "PassengerLoungeSketch1.jpg"
image bg whiteImage = "white.jpg"
image queen = "queen2.jpg"
image pawn = "servant.jpg"
image map = "mapSmallSize.jpg"




label start:
    
    #background image for the main page 
    scene bg detectiveImage
    with fade 
    
    play music "IntroMusic.ogg"  fadeout 2 fadein 2
    #play music
    
    python:
        prompt = "What would you like to do?\n"
        choices = ["Investigate a room", "Talk to a suspect", "Look at your notepad", "Solve the case"]
        
        Game.inputNVL(prompt, choices)
        
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
   
    python:
        prompt = "The [Game.zeppelinName] has 9 rooms.\nWhich would you like to investigate?\n"
        choices = []
        for room in Game.rooms:
            choices.append(room.name);
        
        Game.inputNVL(prompt, choices)
        Game.checkQuit()
        
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
    python:
        prompt = "Which suspect would you like to talk to?\n"
        choices = []
        
        for npc in Game.npcs:
            if npc.alive:
                choices.append(npc.name)
        
        Game.inputNVL(prompt, choices)
        Game.checkQuit()
        
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
        Game.narrateNVL("I don't know which suspect \"[Game.input]\" is.")
        Game.jump("talk_suspect")

label look_notepad:
    
    scene bg notepadImage
    
    python:
        moves = Game.getMoves()
        time = Game.timeString()
        Game.narrateNVL("You've made [moves] move(s). It is now [time].")
        Game.jump("start")

label solve_case:
    python:
        Game.jump("start")
