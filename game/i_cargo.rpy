init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CARGO]
    
    def look():
        Game.inputADV( "A well maintained red steamer trunk. It is embossed with the initials A.R." )
    def open():
        Game.inputADV( "There are neatly pressed clothes with a pile of official looking papers tied with string." )
    redTrunk = Clue( "trunk", [ "look", "open" ], [ look, open ] )
    
    def look():
        # if trunk opens
        Game.inputADV( "It is Colonel Ritter's record of service. It details his commendation for valor at the Details Details Details" )
        # change flag
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
    stop music
    play sound "click.ogg"

    python:
        room = Game.rooms[Game.ROOM_CARGO]
        Game.inputADV("Here we are in the [room.name]! What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_cargo_in:        
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
