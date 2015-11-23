label i_galley:
    scene bg galleyImage
    with fade
    python:
        room = Game.rooms[Game.ROOM_GALLEY]
        
        Game.inputNVL("Here we are in the [room.name]! What do you want to do?")
        Game.checkQuit()
        Game.narrateNVL("I don't know what \"[Game.input]\" means.")
        Game.jump(room.label)