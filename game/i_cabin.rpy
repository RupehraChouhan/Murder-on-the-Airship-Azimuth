init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CABIN]
    Game.cluesFound[Game.CABINS_EMPTY] = False
    
    def look():
        Game.cluesFound[Game.CABINS_EMPTY] = True
        Game.prevNarrate = "Searching among the cabins of the other passengers, you find nothing of interest. The murder weapon must have been stashed somewhere else on the ship."
    room.addCommand("look", look)
    
label i_cabin:
    scene bg cabinImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_CABIN]
        
        # Opening description of the room
        Game.narrateADV("Each room is designed in the same manner as of that of the king's. The mattress as you can see is covered with luxurious silk sheets. . .")
        Game.narrateADV("The ceilings are carefully crafted with shining gold accents and thick plush carpets that caress your feet as you walk.")
        Game.prevNarrate = "What do you want to do?"
        Game.jump(room.label + "_in")
        
label i_cabin_in:        
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
