label t_pawn:
    python:
        NPC.speakADV(NPC.PAWN, "What do you want to say to me?")
        Game.inputADV("Say something:")
        Game.checkQuit()
        NPC.speakADV(NPC.PAWN, "You said \"[Game.input]\"")
        Game.jump("t_pawn")
