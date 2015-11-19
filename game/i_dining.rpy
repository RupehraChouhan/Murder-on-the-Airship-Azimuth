label i_dining:
    python:
        Game.inputNVL("Here we are in the dining room! What do you want to do?")
        Game.checkQuit()
        NPC.speakNVL(NPC.NARRATOR, "I don't know what \"[Game.input]\" means.")
        Game.jump("i_dining")
