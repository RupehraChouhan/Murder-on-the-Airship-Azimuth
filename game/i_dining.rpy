label i_dining:
    scene bg diningImage
    with fade
    python:
        room = Game.rooms[Game.ROOM_DINING]
        
        Game.inputNVL("Here we are in the [room.name]! What do you want to do?")
        Game.checkQuit()
        Game.narrateNVL("I don't know what \"[Game.input]\" means.")
        Game.jump(room.label)