init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_CABIN]
    Game.cluesFound[Game.CABINS_EMPTY] = False
    
    def look():
        Game.cluesFound[Game.CABINS_EMPTY] = True
        Game.narrateADV("Searching among the cabins of the other passengers, you find nothing of interest. The murder weapon must have been stashed somewhere else on the ship.")
    room.addCommand("look", look)

    def look():
        Game.narrateADV( "The largest cabin on the zeppelin, the stateroom was the berth of the Royaumes. Lady Eleanora is here, wearing a sour expression and pretending not to notice you snoop around.")
        Game.narrateADV( "You find nothing of interest.")
    stateroom = Clue( "stateroom", [ "look"], [ look] )
    room.addClue( stateroom )

    def look():
    # If we get around to rook-killing, it would go here.
    # It would look something like "Mr. de la Rocque lies motionless on the floor. By the marks on his neck, it looks like he was strangled from behind. An expensive silk sheet is twisted up under his neck. Looks like that was the weapon."
        Game.narrateADV("Mr. de la Rocque's cabin. He paces nervously, wringing his hands.")
        Game.narrateADV("You find nothing incriminating among his belongings. Just a lot of paperwork.")
    A = Clue( "A", [ "look"], [ look] )
    room.addClue( A )
        
    def look():
        Game.narrateADV( "This is Sergeant-Major Ritter's room. He is a few pages into the {i}Azimuth's{/i} safety manual. He does not react to your presence as you snoop around.")
        Game.narrateADV( "Nothing out of the ordinary. In fact, hardly anything at all. If he brought much luggage, he left it in the hold.")
    B = Clue( "B", [ "look"], [ look] )
    room.addClue( B )

    def look():
        Game.narrateADV("Rector Esgob's room. It smells of liquor and nervous sweat.")
        Game.narrateADV("You don't find anything peculiar though.")
    C = Clue( "C", [ "look"], [ look] )
    room.addClue( C )

    def look():
        Game.narrateADV("This is your cabin. The steward, Polly Newport, is being confined here while you conduct your investigation. She fidgets nervously as you search.")
        Game.narrateADV("You don't find anything you didn't bring aboard.")
    D = Clue( "D", [ "look"], [ look] )
    room.addClue( D )

label i_cabin:
    scene bg cabinImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_CABIN]
        
        # Opening description of the room
        Game.narrateADV("Each room is luxuriously appointed in a baroque style. While the stateroom the Royaumes are travelling in is the grandest, none are short on extravagance. The beds are covered with luxurious silk sheets.")
        Game.narrateADV("The ceilings are carefully crafted with shining gold accents, and thick plush carpets that caress your feet as you walk.")
        Game.narrateADV("Aside from the {b}stateroom{/b}, there are four cabins labelled {b}A{/b}, {b}B{/b}, {b}C{/b}, and {b}D{/b}")
        Game.jump(room.label + "_in")
        
label i_cabin_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.prevNarrate = "What do you want to do?"
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit(room.label + "_in")
        
        try:
            room.do(Game.input)
        except:
            Game.narrateADV("I don't know what \"[Game.input]\" means.")
        
        Game.jump(room.label + "_in")
