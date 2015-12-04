init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_BATHS]
    Game.cluesFound[Game.BATHS_WOUND] = False
    Game.cluesFound[Game.BATHS_TIME_OF_DEATH] = False
    Game.state["baths_body_turned"] = False
    
    def look():
        line = "The large bath is in the middle of the room. The {b}body{/b} of Henry Augustus Algernon Royaume is in a pool of blood from the {b}wound{/b} on his head."
        if Game.state["baths_body_turned"]:
            line += " He is still in his evening wear, now flipped onto his back, his dead eyes staring eerily."
        else:
            line += " He is still in his evening wear, lying face down."
        line += " Blood leads from the body to some {b}towels{/b}."
        Game.prevNarrate = line
    room.addCommand( "look", look )
    
    def look():
        line = "The {b}body{/b} of Henry Augustus Algernon Royaume is in a pool of blood from the {b}wound{/b} on his head."
        if Game.state["baths_body_turned"]:
            line += " He is still in his evening wear, now flipped onto his back, his dead eyes staring eerily."
        else:
            line += " He is still in his evening wear, lying face down."
        Game.prevNarrate = line
    def turn():
        Game.state["baths_body_turned"] = True
        Game.prevNarrate = "You flip over the {b}body{/b}. It looks like there is something in his {b}pocket{/b}."
    body = Clue( "body", [ "look", "turn" ], [ look, turn ] )
    
    def look():
        Game.cluesFound[Game.BATHS_WOUND] = True
        Game.prevNarrate = "Blunt trauma to the head. Based on the fracture pattern, you surmise the {b}wound{/b} was caused by a heavy metal object."
    wound = Clue( "wound" , [ "look" ], [ look ])
    
    def look():
        Game.prevNarrate = "A sparse trail of blood leads from the body to a stack of towels. If this pile was as symmetrical as all the others are, one is missing."
    towels = Clue( "towels" , [ "look" ], [ look ])
    
    def look():
        if Game.state["baths_body_turned"]:
            Game.prevNarrate = "There is something small and round in his {b}pocket{/b}, and possibly some glass shards."
    def open():
        if Game.state["baths_body_turned"]:
            Game.cluesFound[Game.BATHS_TIME_OF_DEATH] = True
            Game.prevNarrate = "Inside his pocket is a silver pocket watch. It must have broken when he fell. The face reads 8:42."
    pocket = Clue( "pocket", [ "look", "open" ], [ look, open ] )
    
    room.addClue(body)
    room.addClue(wound)
    room.addClue(towels)
    room.addClue(pocket)
    
    # clean namespace
    del look
    del turn
    del open

label i_baths:
    scene bg bathImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_BATHS]
        
        # Opening description of the room
        Game.narrateADV("One of the most expensive fittings on the [Game.zeppelinName] is this big bathing hall. Only the finest luxury airships have such a grand amenity.")
        Game.narrateADV("Hot steam fills the air. The ceilings are brilliantly modelled with galvanic bulbs and baroque designs. Four ornamental pillars give a very regal look to the large central basin.")
        Game.narrateADV("Sweet-smelling candles are dotted around, ample stacks of {b}towels{/b} and and multiple doors give a palatial look.")
        Game.prevNarrate = "It would be stunningly impressive if it weren't for the dead man bleeding all over the tile."
        Game.jump(room.label + "_in")
        
label i_baths_in:        
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
