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
            Game.narrateADV( "This is Sergeant-Major Ritter's record of service. It covers his entire military career from enlisted man up to retired war hero." )
            Game.narrateADV( "It seems he got his decorations - and his honourable discharge - from the Battle of Rosenfeldt. Rosenfeldt was a particularly infamous battle in the Third Rurovian Wars." )
            Game.narrateADV( "Her Infallible Majesty's military squabbles never much interested you, but you seem to recall Rosenfeldt had something to do with zeppelins." )
            Game.prevNarrate = "Maybe someone who knows more about aviation can tell you more."
            Game.cluesFound[Game.CARGO_RECORD] = True
    papers = Clue( "papers", [ "look", "read" ], [ look, look ] )
    
    room.addClue(redTrunk)
    room.addClue(papers)
    
    # clean up namespace
    del look
    del open

label i_cargo:
    scene bg cargoHoldImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_CARGO]
        
        # Opening description of the room
        Game.prevNarrate = "You will find a lot of storage here. It contains food supplies, baggages and some extra stock."
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
