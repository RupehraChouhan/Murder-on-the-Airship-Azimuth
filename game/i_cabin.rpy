label i_cabin:
    scene bg cabinImage
    with dissolve
    python:
        room = Game.rooms[Game.ROOM_CABIN]
        
        Game.inputNVL("Here we are in the [room.name]! What do you want to do?")
        Game.checkQuit()
        Game.narrateNVL("I don't know what \"[Game.input]\" means.")
        Game.jump(room.label)