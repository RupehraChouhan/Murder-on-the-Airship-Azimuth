label t_bishop:
    python:
        NPC.speakADV(NPC.BISHOP, "What do you want to say to me?")
        Game.inputADV("Say something:")
        Game.checkQuit()
        NPC.speakADV(NPC.BISHOP, "You said \"[Game.input]\"")
        Game.jump("t_bishop")
