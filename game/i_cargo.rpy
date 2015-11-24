label i_cargo:
    scene bg cargoHoldImage
    with fade
    stop music
    play sound "click.ogg"

    python:
        room = Game.rooms[Game.ROOM_CARGO]
        
        Game.inputNVL("Here we are in the [room.name]! What do you want to do?")
        Game.checkQuit()
        Game.narrateNVL("I don't know what \"[Game.input]\" means.")
        Game.jump(room.label)