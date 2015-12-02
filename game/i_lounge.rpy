init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_LOUNGE]
    Game.cluesFound[Game.LOUNGE_CONTRACTS] = False
    
    def look():
        Game.narrateADV("The lounge is richly appointed with intricate brass fittings and fine mahogany panels. On a writing {b}desk{/b} nearby sit some official-looking {b}documents{/b}.")
    room.addCommand("look", look)

    def look():
        Game.narrateADV( "These documents look important." )
        Game.narrateADV( "On closer inspection, this is a draft of the Royaume & Sons government contract." )
        Game.narrateADV( "Paging through it, though, it doesn't look like Mr. Royaume had signed off on them yet. Mr. de la Rocque's signature is on every page, but the lines for Mr. Royaume's are all blank." )
        Game.cluesFound[Game.LOUNGE_CONTRACTS] = True
    documents = Clue( "documents", [ "look", "read" ], [ look, look ] )
    
    def look():
        Game.narrateADV( "On the writing desk sit some official-looking {b}documents{/b}")
    desk = Clue("desk", ["look"], [look])
    
    room.addClue(documents)
    room.addClue(desk)
    
    del look
    del documents
    del desk

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
        Game.checkQuit(room.label + "_in")
        
        try:
            room.do(Game.input)
        except:
            Game.narrateADV("I don't know what \"[Game.input]\" means.")
        
        Game.jump(room.label + "_in")
