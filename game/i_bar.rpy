label i_bar:
    python:
        Game.inputNVL("Here we are in the bar! What do you want to do?")
        Game.checkQuit()
        NPC.speakNVL(NPC.NARRATOR, "I don't know what \"[Game.input]\" means.")
        Game.jump("i_bar")
