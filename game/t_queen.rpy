label t_queen:
    python:
        NPC.speakADV(NPC.QUEEN, "What do you want to say to me?")
        Game.inputADV("Say something:")
        Game.checkQuit()
        NPC.speakADV(NPC.QUEEN, "You said \"[Game.input]\"")
        Game.jump("t_queen")
