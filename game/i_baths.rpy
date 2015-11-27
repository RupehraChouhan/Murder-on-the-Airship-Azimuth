init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_BATHS]

label i_baths:
    scene bg bathImage
    stop music fadeout 2

    python:
        room = Game.rooms[Game.ROOM_BATHS]
        Game.inputADV("Here we are in the [room.name]! What do you want to do?")
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
