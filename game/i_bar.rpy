init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_BAR]
    
    def look():
        Game.inputADV( "It's a bottle of fine wine!" )
    def drink(): 
        Game.inputADV( "Now is no time to drink, there's a murderer to catch!" )
    def eat():
        Game.inputADV( "What are you, nuts?" )
    bottle = Clue( "bottle", [ "look", "drink", "eat" ], [ look, drink, eat ] )
    room.addClue( bottle )
    
    def look():
        Game.inputADV( "It's a bar, full of bottles" )
    room.addCommand( "look", look )
    
    # clean up namespace
    del look
    del drink
    del eat
    del bottle

label i_bar:
    scene bg barImage
    with fade
    stop music fadeout 2

    python:
        room = Game.rooms[Game.ROOM_BAR]
        Game.inputADV("Here we are in the [room.name]! What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_bar_in:        
    python:
        # assumption: if all functions of clues are inputADV, then we can loop through this
        Game.checkQuit()
        
        if Game.input == "":
            Game.inputADV( Game.prevPrompt )
        else:
            try:
                room.do(Game.input)
            except:
                Game.narrateADV("I don't know what \"[Game.input]\" means.")
                Game.inputADV( Game.prevPrompt )
        
        Game.jump(room.label + "_in")
