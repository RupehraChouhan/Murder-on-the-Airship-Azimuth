init 0 python:  
    Game.initialize()

# The game starts here
label start:
    python:
        button = nvl_menu([("Investigate a room.", 0), ("Talk to a suspect.", 1), ("Look at your notepad.", 2), ("Solve the case.", 3)])
        if button == 0: Game.jump("investigate_room")
        if button == 1: Game.jump("talk_suspect")
        if button == 2: Game.jump("look_notepad")
        if button == 3: Game.jump("solve_case")
        Game.jump("start")

label investigate_room:
    python:
        Game.inputNVL("What room do you want to investigate?")
        Game.checkQuit()
        for r in Game.rooms:
            if r.match(Game.input):
                Game.incrementMoves() # Heading to a room counts as a move
                Game.jump(r.label)
        Game.narrate("I don't know what room \"[Game.input]\" is.")
        Game.jump("investigate_room")

label talk_suspect:
    python:
        Game.inputNVL("Which suspect do you want to talk to?")
        Game.checkQuit()
        for n in Game.npcs:
            if n.match(Game.input) and n.label: # We can't talk to them if they don't have a label to jump to
                Game.incrementMoves() # Talking to a suspect counts as a move
                Game.jump(n.label)
        Game.narrate("I don't know which suspect \"[Game.input]\" is.")
        Game.jump("talk_suspect")

label look_notepad:
    python:
        moves = Game.getMoves()
        Game.narrate("You've made [moves] move(s).")
        Game.jump("start")

label solve_case:
    python:
        Game.jump("start")
