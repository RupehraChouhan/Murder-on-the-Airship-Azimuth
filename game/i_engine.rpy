init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_ENGINE]
    Game.state["engine_left_machine_open"] = False
    Game.state[Game.STATE_ENGINE_MISSING_PIPE] = False
    
    def look():
        Game.prevNarrate = "The entire room is alive with noise and light. There are three large {b}machines{/b} in the room, each with a brass {b}plaque{/b} mounted beside them. Off to the side is a {b}rack{/b} of {b}tools{/b}."
    room.addCommand("look", look)
    
    def look():
        Game.prevNarrate = "There are three {b}plaques{/b} in the room: {b}left{/b}, {b}right{/b}, and {b}middle{/b}"
    plaque = Clue("plaque", [ "look", "read" ], [ look, look ] )
    plaques = Clue("plaques", [ "look", "read" ], [ look, look ] )
   
    def look():
        Game.prevNarrate = "The {b}left plaque{/b} reads \"RESPONSONOMIC BARO-DEREGULATOR\"."
    leftPlaque = Clue("left plaque", [ "look", "read" ], [ look, look ] )
    plaqueLeft = Clue("plaque left", [ "look", "read" ], [ look, look ] )
    
    def look():
        Game.prevNarrate = "The {b}right plaque{/b} reads \"TRANSTHERMAL DYNACOUPLING\"."
    rightPlaque = Clue("right plaque", [ "look", "read" ], [ look, look ] )
    plaqueRight = Clue("plaque right", [ "look", "read" ], [ look, look ] )
    
    def look():
        Game.prevNarrate = "The {b}middle plaque{/b} reads \"GALVANIC POLYAGGREGATOR\"."
    middlePlaque = Clue("middle plaque", [ "look", "read" ], [ look, look ] )
    plaqueMiddle = Clue("plaque middle", [ "look", "read" ], [ look, look ] )
    
    def look():
        Game.prevNarrate = "There are three {b}machines{/b} in the room: {b}left{/b}, {b}right{/b}, and {b}middle{/b}"
    machine = Clue( "machine", [ "look" ], [ look ] )
    machines = Clue( "machines", [ "look" ], [ look ] )
    
    def look():
        Game.prevNarrate = "You look at the {b}machine{/b} on the {b}left{/b}. It's a big machine with a bunch of pipes coming out the top. There's a whistling noise coming from inside."
    def open():
        Game.prevNarrate = "There is a crazy tangle of {b}pipes{/b} inside. You find that the whistle is coming from where a two foot length of pipe is missing."
        Game.state["engine_left_machine_open"] = True
        Game.state[Game.STATE_ENGINE_MISSING_PIPE] = True
    leftMachine = Clue("left machine", [ "look", "open" ], [ look, open ] )
    machineLeft = Clue("machine left", [ "look", "open" ], [ look, open ] )
    
    def look():
        Game.prevNarrate = "You look at the {b}machine{/b} on the {b}right{/b}. This big, mysterious machine emanates an infernal heat."
    def open():
        Game.prevNarrate = "What are you, crazy?! It's way too hot to try to open!"
    rightMachine = Clue("right machine", [ "look", "open" ], [ look, open ] )
    machineRight = Clue("machine right", [ "look", "open" ], [ look, open ] )
    
    def look():
        Game.prevNarrate = "You look at the {b}machine{/b} in the {b}middle{/b}. Electricity crackles between two silver spheres protruding from the top of this complex-looking machine."
    def open():
        Game.prevNarrate = "It looks pretty dangerous, you probably shouldn't try to open it."
    middleMachine = Clue("middle machine", [ "look", "open" ], [ look, open ] )
    machineMiddle = Clue("machine middle", [ "look", "open" ], [ look, open ] )
    
    def look():
        line = "A rack of neatly sorted wrenches appear to be perfectly in place. Nothing seems to be missing."
        if Game.cluesFound[Game.BATHS_WOUND]:
            line += " This could be the murder weapon, if the killer put it back afterwards."
        Game.prevNarrate = line
    tools = Clue("tools", [ "look" ], [ look ] )
    rack = Clue("rack", [ "look" ], [ look ] )
    tool_rack = Clue("tool rack", [ "look" ], [ look ] )
    
    def look():
        if Game.state["engine_left_machine_open"]:
            line = "One of the steam {b}pipes{/b} inside this machine is missing, causing it to emit a shrill whistle."
            if Game.cluesFound[Game.BATHS_WOUND]:
                line += "This could very well be the murder weapon, wherever it is."
            Game.prevNarrate = line
    pipes = Clue("pipes", [ "look" ], [ look ] )
    
    room.addClue(plaque)
    room.addClue(plaques)
    room.addClue(leftPlaque)
    room.addClue(rightPlaque)
    room.addClue(middlePlaque)
    room.addClue(plaqueLeft)
    room.addClue(plaqueRight)
    room.addClue(plaqueMiddle)
    
    room.addClue(machine)
    room.addClue(machines)
    room.addClue(leftMachine)
    room.addClue(rightMachine)
    room.addClue(middleMachine)
    room.addClue(machineLeft)
    room.addClue(machineRight)
    room.addClue(machineMiddle)
    
    room.addClue(tools)
    room.addClue(rack)
    room.addClue(tool_rack)
    room.addClue(pipes)
    
    # clean up namespace
    del look
    del open

label i_engine:
    scene bg engineImage
    with fade
    
    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_ENGINE]
        
        # Opening description of the room
        Game.narrateADV("The engine room is overwhelmingly hot and loud, and the smell of exhaust and grease is potent.")
        Game.narrateADV("These engines are huge, and they look brand new, no penny was wasted down here.")
        Game.prevNarrate = "Passengers aren't supposed to be here, but you have a job to do."
        Game.jump(room.label + "_in")
        
label i_engine_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit(room.label + "_in")
        
        try:
            room.do(Game.input.lower())
        except:
            temp = Game.prevNarrate
            Game.narrateADV("I don't know what \"[Game.input]\" means.")
            Game.prevNarrate = temp
        
        Game.jump(room.label + "_in")
