init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_GALLEY]
    
    def look():
        Game.inputADV( "There appears to be a screw missing from the vent." )
    def open():
        Game.inputADV( "Inside the vent there is a bloody pipe!!!!" )
    vent = Clue( "vent", [ "look", "open" ], [ look, open ] )
    
    def look():
        # if opened vent
        Game.inputADV( "The pipe is covered in fresh blood. Definitely our murder weapon." )
        # Change flag
    pipe = Clue( "pipe", [ "look" ], [ look ] )
    
    def look():
        Game.inputADV( "A revolutionary tract" )
        # change flag
    book = Clue( "book", [ "look", "read" ], [ look, look ] )
    
    room.addClue(vent)
    room.addClue(book)
    room.addClue(pipe)
    
    del look
    del open
    del pipe
    del vent

label i_galley:
    scene bg galleyImage
    with fade
    stop music fadeout 2

    python:
        room = Game.rooms[Game.ROOM_GALLEY]
        Game.inputADV("Here we are in the [room.name]! What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_galley_in:        
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
