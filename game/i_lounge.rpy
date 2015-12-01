init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_LOUNGE]
    Game.cluesFound[Game.LOUNGE_CONTRACTS] = False
    
    def look():
        Game.narrateADV("The lounge is richly appointed with intricate brass fittings and fine mahogany panels. On a writing desk nearby sit some official-looking documents.")
    room.addCommand("look", look)

    def look():
        Game.narrateADV( "These documents look important." )
        Game.narrateADV( "On closer inspection, this is a draft of the Royaume & Sons government contract." )
        Game.narrateADV( "Paging through it, though, it doens't look like Mr. Royaume had signed off on them yet. Mr. de la Rocque's signature is on every page, but the lines for Mr. Royaume's are all blank." )
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
        Game.narrateADV("The lounge is the biggest room on the {i}Azimuth{/i}. People come here to interact and relax.")
        Game.narrateADV("What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_lounge_in:        
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
