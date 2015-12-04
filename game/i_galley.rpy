init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_GALLEY]
    Game.cluesFound[Game.GALLEY_PIPE] = False
    Game.cluesFound[Game.GALLEY_BOOK] = False
    Game.state["galley_vent_open"] = False
    
    def look():
        Game.prevNarrate = "The galley hums as assorted contraptions wash the dishes from the evening's meal. However, some details jump out to your keen detective senses. There is a {b}book{/b} lying on the counter, and something seems off about one of the {b}vent{/b}s above the stove."
    room.addCommand("look", look)
    
    def look():
        Game.prevNarrate = "There appears to be a screw missing from the {b}vent{/b}."
    def open():
        Game.state["galley_vent_open"] = True
        Game.prevNarrate = "Inside the vent there is a length of {b}pipe{/b} wrapped in a bloody towel!"
        Game.cluesFound[Game.GALLEY_PIPE] = True
    vent = Clue( "vent", [ "look", "open", "unscrew" ], [ look, open, open ] )
    
    def look():
        if Game.state["galley_vent_open"]:
            Game.prevNarrate = "The {b}pipe{/b} is covered in fresh blood. Definitely our murder weapon."
    pipe = Clue( "pipe", [ "look" ], [ look ] )
    
    def look():
        Game.narrateADV( "This is a copy of THE WORKER'S CALL TO ARMS - MEDITATIONS ON THE PLIGHT OF THE LABOURING CLASSES by Maximilian Singer." )
        Game.prevNarrate = "An infamous revolutionary political tract. Singerists have committed numerous acts of sabotage at industrial sites around the country. You have turned down more than your fair share of industrialists asking you to ferret out Singerists among their workforces."
        Game.cluesFound[Game.GALLEY_BOOK] = True
    book = Clue( "book", [ "look", "read" ], [ look, look ] )
    
    room.addClue(vent)
    room.addClue(pipe)
    room.addClue(book)
    
    # clean up namespace
    del look
    del open

label i_galley:
    scene bg galleyImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_GALLEY]
        
        # Opening description of the room
        Game.narrateADV("All the food is prepared here. It is uncomfortably quiet right now but the smell of fresh food and spices consume the air.")
        Game.prevNarrate = "Each stove, countertop, pot, pan, and sink glows as the light shines on its expensive metals."
        Game.jump(room.label + "_in")
        
label i_galley_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit(room.label + "_in")
        
        try:
            room.do(Game.input.lower())
        except:
            temp = Game.prevNarrate
            Game.narrateADV("I don't know what \"[Game.input]\" means.")
            Game.prevNarrate = temp
        
        Game.jump(room.label + "_in")
