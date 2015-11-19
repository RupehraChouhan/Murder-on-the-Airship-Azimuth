label i_cargo:
    python:
        Game.inputNVL("Here we are in the cargo hold! What do you want to do?")
        Game.checkQuit()
        NPC.speakNVL(NPC.NARRATOR, "I don't know what \"[Game.input]\" means.")
        Game.jump("i_cargo")
