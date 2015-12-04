init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CARGO]
    Game.cluesFound[Game.CARGO_RECORD] = False
    Game.state["cargo_trunk_open"] = False
    
    def look():
        Game.narrateADV("The cargo hold if filled with supplies, as well as the {b}trunk{/b}s of the other passengers")
    room.addCommand("look", look)
    
    def look():
        Game.narrateADV( "A well maintained red steamer trunk. It is embossed with the initials A.R." )
    def open():
        Game.narrateADV( "There are neatly pressed clothes with a pile of official looking papers tied with string." )
        Game.state["cargo_trunk_open"] = True
    redTrunk = Clue( "trunk", [ "look", "open" ], [ look, open ] )
    
    def look():
        if Game.state["cargo_trunk_open"]:
            Game.narrateADV( "This is Sergeant-Major Ritter's record of service. It covers his entire military career from enlisted man up to retired war hero." )
            Game.narrateADV( "It seems he got his decorations - and his honourable discharge - from the Battle of Rosenfeldt. Rosenfeldt was a particularly infamous battle in the Third Rurovian Wars." )
            Game.narrateADV( "Her Infallible Majesty's military squabbles never much interested you, but you seem to recall Rosenfeldt had something to do with zeppelins." )
            Game.narrateADV( "Maybe someone who knows more about aviation can tell you more." )
            Game.cluesFound[Game.CARGO_RECORD] = True
        else:
            raise Error()
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
