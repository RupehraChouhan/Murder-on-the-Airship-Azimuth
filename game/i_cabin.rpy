init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CABIN]
    Game.cluesFound[Game.CABINS_EMPTY] = False
    Game.state["cabin_stateroom"] = False
    Game.state["cabin_A"] = False
    Game.state["cabin_B"] = False
    Game.state["cabin_C"] = False
    Game.state["cabin_D"] = False

    def searchedAllCabins():
        if Game.state["cabin_stateroom"] and Game.state["cabin_A"] and Game.state["cabin_B"] and Game.state["cabin_C"] and Game.state["cabin_D"]:
            Game.cluesFound[Game.CABINS_EMPTY] = True
            return " Having found nothing in all of the rooms here, you conclude the murder weapon must have been stashed somewhere else on the ship."
        else:
            return ""
    
    def look():
        Game.prevNarrate = "Aside from the {b}stateroom{/b}, there are four cabins labelled {b}A{/b}, {b}B{/b}, {b}C{/b}, and {b}D{/b}."
    room.addCommand("look", look)

    def look():
        Game.state["cabin_stateroom"] = True
        Game.narrateADV( "The largest cabin on the zeppelin, the stateroom was the berth of the Royaumes. Lady Eleanora is here, wearing a sour expression and pretending not to notice you snoop around.")
        Game.prevNarrate = "You find nothing of interest."
        Game.prevNarrate += searchedAllCabins()
    stateroom = Clue( "stateroom", [ "look" ], [ look ] )
    state = Clue( "state", [ "look" ], [ look ] )

    def look():
    # If we get around to rook-killing, it would go here.
    # It would look something like "Mr. de la Rocque lies motionless on the floor. By the marks on his neck, it looks like he was strangled from behind. An expensive silk sheet is twisted up under his neck. Looks like that was the weapon."
        Game.state["cabin_A"] = True
        Game.narrateADV("Mr. de la Rocque's cabin. He paces nervously, wringing his hands.")
        Game.prevNarrate = "You find nothing incriminating among his belongings. Just a lot of paperwork."
        Game.prevNarrate += searchedAllCabins()
    A = Clue( "A", [ "look" ], [ look ] )
        
    def look():
        Game.state["cabin_B"] = True
        Game.narrateADV( "This is Sergeant-Major Ritter's room. He is a few pages into the {i}Azimuth's{/i} safety manual. He does not react to your presence as you snoop around.")
        Game.prevNarrate = "Nothing out of the ordinary. In fact, hardly anything at all. If he brought much luggage, he left it in the hold."
        Game.prevNarrate += searchedAllCabins()
    B = Clue( "B", [ "look" ], [ look ] )

    def look():
        Game.state["cabin_C"] = True
        Game.narrateADV("Rector Esgob's room. It smells of liquor and nervous sweat.")
        Game.prevNarrate = "You don't find anything peculiar though."
        Game.prevNarrate += searchedAllCabins()
    C = Clue( "C", [ "look" ], [ look ] )

    def look():
        Game.state["cabin_D"] = True
        Game.narrateADV("This is your cabin. The steward, Polly Newport, is being confined here while you conduct your investigation. She fidgets nervously as you search.")
        Game.prevNarrate = "You don't find anything you didn't bring aboard."
        Game.prevNarrate += searchedAllCabins()
    D = Clue( "D", [ "look" ], [ look ] )

    room.addClue(stateroom)
    room.addClue(state)
    room.addClue(A)
    room.addClue(B)
    room.addClue(C)
    room.addClue(D)
    
    # clean namespace
    del look
    
label i_cabin:
    scene bg cabinImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_CABIN]
        
        # Opening description of the room
        Game.narrateADV("Each room is luxuriously appointed in a baroque style. While the stateroom the Royaumes are travelling in is the grandest, none are short on extravagance. The beds are covered with luxurious silk sheets.")
        Game.prevNarrate = "The ceilings are carefully crafted with shining gold accents, and thick plush carpets that caress your feet as you walk."
        Game.jump(room.label + "_in")
        
label i_cabin_in:        
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
