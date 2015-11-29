init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CABIN]
    
label i_cabin:
    scene bg cabinImage
    with fade
    stop music fadeout 2

    python:
        room = Game.rooms[Game.ROOM_CABIN]
        Game.narrateADV("Here we are in the [room.name]!")
        Game.narrateADV("Each room is designed in the same manner as of that of the king's. The mattress as you can see is covered with luxurious silk sheets. . .")
        Game.narrateADV("The ceilings are carefully crafted with shining gold accents and thick plush carpets that caress your feet as you walk.")
        Game.inputADV("What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_cabin_in:        
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
