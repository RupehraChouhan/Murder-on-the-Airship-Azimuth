init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_BAR]
    
    def look():
        Game.narrateADV( "It's a bottle of fine wine!" )
    def drink(): 
        Game.narrateADV( "Now is no time to drink, there's a murderer to catch!" )
    def eat():
        Game.narrateADV( "What are you, nuts?" )
    bottle = Clue( "bottle", [ "look", "drink", "eat" ], [ look, drink, eat ] )
    room.addClue( bottle )
    
    def look():
        Game.narrateADV( "It's a bar, full of bottles" )
    room.addCommand( "look", look )
    
    # clean up namespace
    del look
    del drink
    del eat
    del bottle

label i_bar:
    scene bg barImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_BAR]
        
        # Opening description of the room
        Game.narrateADV("There is a wide collection of drinks here ranging from very expensive to very old bottles..")
        Game.narrateADV("There is also a big sitting area with tables and chairs very similar to the lounge. But remember it's time to work and find out the culprit!")
        Game.jump(room.label + "_in")
        
label i_bar_in:        
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
