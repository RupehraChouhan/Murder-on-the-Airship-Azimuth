label t_rook:
    python:
        NPC.speakADV(NPC.ROOK, "What do you want to say to me?")
        Game.inputADV("Say something:")
        Game.checkQuit()
        NPC.speakADV(NPC.ROOK, "You said \"[Game.input]\"")
        Game.jump("t_rook")
