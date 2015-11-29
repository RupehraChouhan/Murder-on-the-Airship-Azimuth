init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_GALLEY]
    Game.cluesFound[Game.GALLEY_PIPE] = False
    Game.cluesFound[Game.GALLEY_BOOK] = False
    Game.state["galley_vent_open"] = False
    
    def look():
        Game.narrateADV( "There appears to be a screw missing from the vent." )
    def open():
        Game.state["galley_vent_open"] = True
        Game.narrateADV( "Inside the vent there is a bloody pipe!!!!" )
        Game.cluesFound[Game.GALLEY_PIPE] = True
    vent = Clue( "vent", [ "look", "open" ], [ look, open ] )
    
    def look():
        if Game.state["galley_vent_open"]:
            Game.narrateADV( "The pipe is covered in fresh blood. Definitely our murder weapon." )
    pipe = Clue( "pipe", [ "look" ], [ look ] )
    
    def look():
        Game.narrateADV( "A revolutionary tract" )
        Game.cluesFound[Game.GALLEY_BOOK] = True
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
        Game.narrateADV("Here we are in the [room.name]!")
        Game.narrateADV("All the food is prepared here.It is uncomfortably quiet right now but the smell of fresh food and spices consume the air.")
        Game.narrateADV("Each stove, countertop, pot, pan, and sink glows as the light shines on its expensive metals.")
        Game.narrateADV("What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_galley_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit()
        
        if Game.input != "":
            try:
                room.do(Game.input)
            except:
                Game.narrateADV("I don't know what \"[Game.input]\" means.")
        
        Game.jump(room.label + "_in")
