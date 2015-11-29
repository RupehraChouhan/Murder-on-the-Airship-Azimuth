init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_LOUNGE]
    Game.cluesFound[Game.LOUNGE_CONTRACTS] = False
    
    def look():
        Game.inputADV( "These documents look important" )
        Game.cluesFound[Game.LOUNGE_CONTRACTS] = True
    documents = Clue( "documents", [ "look", "read" ], [ look, look ] )
    
    room.addClue(documents)
    
    del look
    del documents

label i_lounge:
    scene bg loungeImage
    with fade 
    stop music fadeout 2

    python:
        room = Game.rooms[Game.ROOM_LOUNGE]
        Game.narrateADV("Here we are in the [room.name]!")
        Game.narrateADV("Lounge is the biggest room on the Zeppelin. People come here to interact and relax. ")
        Game.inputADV("What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_lounge_in:        
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
