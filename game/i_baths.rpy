label i_baths:
    python:
        Game.inputNVL("Here we are in the baths! What do you want to do?")
        Game.checkQuit()
        NPC.speakNVL(NPC.NARRATOR, "I don't know what \"[Game.input]\" means.")
        Game.jump("i_baths")
