init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_ENGINE]
    
    def look():
        Game.inputADV( "There are three plaques in the room: left, right, and middle" )    
    plaque = Clue("plaque", [ "look", "read" ], [ look, look ] )
    
    def look():
        Game.inputADV( "RESPONSONOMIC BARO-DEREGULATOR" )
    leftPlaque = Clue("left plaque", [ "look", "read" ], [ look, look ] )
    
    def look():
        Game.inputADV( "TRANSTHERMAL DYNACOUPLING" )
    rightPlaque = Clue("right plaque", [ "look", "read" ], [ look, look ] )
    
    def look():
        Game.inputADV( "GALVANIC POLYAGGREGATOR" )
    middlePlaque = Clue("middle plaque", [ "look", "read" ], [ look, look ] )
    
    def look():
        Game.inputADV( "There are three machines: left, right, and middle" )
    machine = Clue( "machine", [ "look" ], [ look ] )
    
    def look():
        Game.inputADV( "It's a big machine with a bunch of pipes coming out the top. There's a whistling noise coming from inside." )
    def open():
        Game.inputADV( "There is a crazy tangle of pipes inside. You find that the whistle is coming from where a 2 foot length of pipe is missing." )
    leftMachine = Clue("left machine", [ "look", "open" ], [ look, open ] )
    
    def look():
        Game.inputADV( "This big, mysterious machine emanates an infernal heat." )
    # something else to do
    rightMachine = Clue("right machine", [ "look" ], [ look ] )
    
    def look():
        Game.inputADV( "Electricity crackles between two silver spheres protruding from the top of this machine" )
    # fluff
    middleMachine = Clue("middle machine", [ "look" ], [ look ] )
    
    def look():
        Game.inputADV( "A rack of neatly sorted wrenches appear to be perfectly in place. Nothing seems to be missing." )
        # if you've looked at the wound, suggest this could be the murder weapon if they put it back afterwards
    tools = Clue("tools", [ "look" ], [ look ] )
    
    def look():
        # require machine to be open
        Game.inputADV( "One of the steam pipes inside this machine is missing, causing it to emit a shrill whistle." )
        # if you've looked at the wound, suggest this could be the murder weapon
    pipes = Clue("pipes", [ "look" ], [ look ] )
    
    room.addClue(plaque)
    room.addClue(leftPlaque)
    room.addClue(rightPlaque)
    room.addClue(middlePlaque)
    room.addClue(machine)
    room.addClue(leftMachine)
    room.addClue(rightMachine)
    room.addClue(middleMachine)
    room.addClue(tools)
    room.addClue(pipes)
    
    del plaque
    del leftPlaque
    del rightPlaque
    del middlePlaque
    del machine
    del leftMachine
    del rightMachine
    del middleMachine
    del tools
    del pipes
    del look
    del open

label i_engine:
    scene bg engineImage
    with fade 
    stop music fadeout 2
    
    python:
        room = Game.rooms[Game.ROOM_ENGINE]
        Game.inputADV("Here we are in the [room.name]! What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_engine_in:        
    python:
        # assumption: if all functions of clues are inputADV, then we can loop through this
        Game.checkQuit()
        
        if Game.input == "":
            Game.inputADV( Game.prevPrompt )
        else:
            try:
                room.do(Game.input)
            except:
                Game.narrateADV("I don't know what \"[Game.input]\" means.")
                Game.inputADV( Game.prevPrompt )
        
        Game.jump(room.label + "_in")
