init 0 python:
    bottle = Clue("bottle", ["look"], [lambda : Game.narrateNVL("It's a bottle")])

label i_bar:
    scene bg barImage
    stop music
    play sound "click.ogg"

    python:
        room = Game.rooms[Game.ROOM_BAR]
        
        bottle.do("look")
        
        Game.inputNVL("Here we are in the [room.name]! What do you want to do?")
        Game.checkQuit()
        Game.narrateNVL("I don't know what \"[Game.input]\" means.")
        Game.jump(room.label)
