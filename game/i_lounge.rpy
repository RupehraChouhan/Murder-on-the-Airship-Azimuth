init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_LOUNGE]
    Game.cluesFound[Game.LOUNGE_CONTRACTS] = False
    
    def look():
        Game.narrateADV( "These documents look important" )
        Game.cluesFound[Game.LOUNGE_CONTRACTS] = True
    documents = Clue( "documents", [ "look", "read" ], [ look, look ] )
    
    room.addClue(documents)
    
    del look
    del documents

label i_lounge:
    scene bg loungeImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_LOUNGE]
        
        # Opening description of the room
        Game.narrateADV("The lounge is the biggest room on the [Game.zeppelinName]. People come here to interact and relax. ")
        Game.jump(room.label + "_in")
        
label i_lounge_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.prevNarrate = "What do you want to do?"
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit()
        
        if Game.input != "":
            try:
                room.do(Game.input)
            except:
                Game.narrateADV("I don't know what \"[Game.input]\" means.")
        
        Game.jump(room.label + "_in")
