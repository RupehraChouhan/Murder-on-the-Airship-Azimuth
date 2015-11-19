label t_knight:
    python:
        NPC.speakADV(NPC.KNIGHT, "What do you want to say to me?")
        Game.inputADV("Say something:")
        Game.checkQuit()
        NPC.speakADV(NPC.KNIGHT, "You said \"[Game.input]\"")
        Game.jump("t_knight")
