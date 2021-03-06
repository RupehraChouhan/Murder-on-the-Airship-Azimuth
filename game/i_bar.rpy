init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_BAR]
    
    def look():
        Game.prevNarrate = "The wall is almost full of a large assortment of fine wine and brandy {b}bottle{/b}s. The bartender who was serving here must have retired to bed when the passengers were confined to their cabins."
    room.addCommand( "look", look )
    
    def look():
        Game.prevNarrate = "It's a {b}bottle{/b} of fine {b}brandy{/b}. Mostly empty."
    def drink(): 
        Game.prevNarrate = "Now is no time to drink, there's a murderer to catch!"
    def eat():
        Game.prevNarrate = "What are you, nuts?"
    bottle = Clue( "bottle", [ "look", "drink", "eat" ], [ look, drink, eat ] )
    brandy = Clue( "brandy", [ "look", "drink", "eat" ], [ look, drink, eat ] )
    
    room.addClue(bottle)
    room.addClue(brandy)
    
    # clean up namespace
    del look
    del drink
    del eat

label i_bar:
    scene bg barImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_BAR]
        
        # Opening description of the room
        Game.narrateADV("There is a wide collection of drinks here ranging from very expensive to very old bottles.")
        Game.prevNarrate = "There is also a big sitting area with tables and chairs very similar to the lounge. But remember it's time to work and find out the culprit!"
        Game.jump(room.label + "_in")
        
label i_bar_in:        
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
