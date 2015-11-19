init 0 python:
    # NPC, array of NPCs, and constants defined in NPC.rpy
    NPC.npc[NPC.KING] = NPC("King", None, "#ffffff", []) # White
    NPC.npc[NPC.QUEEN] = NPC("Queen", "t_queen", "#ff0000", []) # Red
    NPC.npc[NPC.BISHOP] = NPC("Bishop", "t_bishop", "#00ff00", []) # Green
    NPC.npc[NPC.KNIGHT] = NPC("Knight", "t_knight", "#0000ff", []) # Blue
    NPC.npc[NPC.ROOK] = NPC("Rook", "t_rook", "#ffff00", []) # Yellow
    NPC.npc[NPC.PAWN] = NPC("Pawn", "t_pawn", "#00ffff", []) # Cyan
    
    # Room, array of rooms, and constants defined in Room.rpy
    Room.room[Room.CABIN] = Room("Passenger Cabins", "i_cabin", 0, 0, [])
    Room.room[Room.DINING] = Room("Dining Room", "i_dining", 1, 0, [])
    Room.room[Room.GALLEY] = Room("Galley", "i_galley", 2, 0, [])
    Room.room[Room.BATHS] = Room("Baths", "i_baths", 0, 1, [])
    Room.room[Room.LOUNGE] = Room("Passenger Lounge", "i_lounge", 1, 1, [])
    Room.room[Room.BAR] = Room("Bar", "i_bar", 2, 1, [])
    Room.room[Room.CARGO] = Room("Cargo Hold", "i_cargo", 0, 2, [])
    Room.room[Room.COCKPIT] = Room("Cockpit", "i_cockpit", 1, 2, [])
    Room.room[Room.ENGINE] = Room("Engine Room", "i_engine", 2, 2, [])

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
        for r in Room.room:
            if r.match(Game.input):
                Game.incrementMoves() # Heading to a room counts as a move
                Game.jump(r.label)
        NPC.speakNVL(NPC.NARRATOR, "I don't know what room \"[Game.input]\" is.")
        Game.jump("investigate_room")

label talk_suspect:
    python:
        Game.inputNVL("Which suspect do you want to talk to?")
        Game.checkQuit()
        for n in NPC.npc:
            if n.match(Game.input) and n.label: # We can't talk to them if they don't have a label to jump to
                Game.incrementMoves() # Talking to a suspect counts as a move
                Game.jump(n.label)
        NPC.speakNVL(NPC.NARRATOR, "I don't know which suspect \"[Game.input]\" is.")
        Game.jump("talk_suspect")

label look_notepad:
    python:
        moves = Game.getMoves()
        NPC.speakNVL(NPC.NARRATOR, "You've made [moves] move(s).")
        Game.jump("start")

label solve_case:
    python:
        Game.jump("start")
