init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_COCKPIT]

label i_cockpit:
    scene bg cockPitImage
    with fade
    stop music
    play sound "click.ogg"

    python:
        room = Game.rooms[Game.ROOM_COCKPIT]
        Game.inputADV("Here we are in the [room.name]! What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_cockpit_in:        
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
