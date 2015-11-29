init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_BATHS]
    
    def look():
        Game.inputADV( "The body of Henry Augustus Algernon Royaume is in a pool of blood from the wound on his head. He is still in his evening wear, lying face down. " )
    def turn():
        Game.inputADV( "You flip over the body. It looks like there is something in his pocket." )
    body = Clue( "body", [ "look", "turn" ], [ look, turn ] )
    
    def look():
        Game.inputADV( "The wound appears to be caused by a heavy metal object." )
        # Change flag
    wound = Clue( "wound" , [ "look" ], [ look ])
    
    def look():
        Game.inputADV( "There is something small and round in his pocket, and possibly some glass shards" )
    def open():
        Game.inputADV( "Inside his pocket is a silver pocket watch. It must have broken when he fell. The face reads 8:42" )
        # Change flag
    pocket = Clue( "pocket", [ "look", "open" ], [ look, open ] )
    
    room.addClue(body)
    room.addClue(wound)
    room.addClue(pocket)
    
    def look():
        Game.inputADV( "There's the body" )
    room.addCommand( "look", look )
    
    # clean namespace
    del look
    del body

label i_baths:
    scene bg bathImage
    stop music fadeout 2

    python:
        room = Game.rooms[Game.ROOM_BATHS]
        Game.inputADV("Here we are in the [room.name]One of the most expensive places on this Zeppelin is this big bath. This was created especially on queen's demand. Rich people can do anything in the world you know!! What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_baths_in:        
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
