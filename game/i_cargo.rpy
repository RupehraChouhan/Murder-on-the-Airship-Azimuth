init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CARGO]
    Game.cluesFound[Game.CARGO_RECORD] = False
    Game.state["cargo_trunk_open"] = False
    
    def look():
        Game.prevNarrate = "The cargo hold if filled with supplies, as well as the {b}trunk{/b}s of the other passengers."
    room.addCommand("look", look)
    
    def look():
        Game.prevNarrate = "A well maintained red steamer {b}trunk{/b}. It is embossed with the initials A.R."
    def open():
        Game.prevNarrate = "There are neatly pressed clothes with a pile of official looking {b}papers{/b} tied with string."
        Game.state["cargo_trunk_open"] = True
    redTrunk = Clue( "trunk", [ "look", "open" ], [ look, open ] )
    
    def look():
        if Game.state["cargo_trunk_open"]:
            Game.prevNarrate = "It is Colonel Ritter's record of service. It details his commendation for valor at the Battle of Rosenfeldt, and other notable achievements."
            Game.cluesFound[Game.CARGO_RECORD] = True
    papers = Clue( "papers", [ "look", "read" ], [ look, look ] )
    
    room.addClue(redTrunk)
    room.addClue(papers)
    
    del redTrunk
    del papers
    del look
    del open

label i_cargo:
    scene bg cargoHoldImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_CARGO]
        
        # Opening description of the room
        Game.narrateADV("You will find a lot of storage here. It contains food supplies, baggages and some extra stock.")
        Game.prevNarrate = "What do you want to do?"
        Game.jump(room.label + "_in")
        
label i_cargo_in:        
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
