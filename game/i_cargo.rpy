init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CARGO]
    Game.cluesFound[Game.CARGO_RECORD] = False
    Game.state["cargo_trunk_open"] = False
    
    def look():
        Game.narrateADV( "A well maintained red steamer trunk. It is embossed with the initials A.R." )
    def open():
        Game.narrateADV( "There are neatly pressed clothes with a pile of official looking papers tied with string." )
        Game.state["cargo_trunk_open"] = True
    redTrunk = Clue( "trunk", [ "look", "open" ], [ look, open ] )
    
    def look():
        # if trunk opens
        Game.narrateADV( "It is Colonel Ritter's record of service. It details his commendation for valor at the Details Details Details" )
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
        Game.jump(room.label + "_in")
        
label i_cargo_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.prevNarrate = "What do you want to do?"
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit(room.label + "_in")
        
        try:
            room.do(Game.input)
        except:
            Game.narrateADV("I don't know what \"[Game.input]\" means.")
        
        Game.jump(room.label + "_in")
