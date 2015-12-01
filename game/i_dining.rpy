init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_DINING]
    Game.cluesFound[Game.DINING_SPECTACLES] = False
    
    def look():
        Game.narrateADV( "These glasses appear to belong to the bishop *changeme*" )
        Game.cluesFound[Game.DINING_SPECTACLES] = True
    glasses = Clue( "glasses", [ "look" ], [ look ] )

label i_dining:
    scene bg diningImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_DINING]
        
        # Opening description of the room
        Game.narrateADV("The dining room, where everyone had supper at 7pm. The king was last seen alive here.")
        Game.narrateADV("It is a massive room with big windows on the side providing a very beautiful view of the outside.")
        Game.narrateADV("The dining tables are covered with graceful white cloth where the passengers are served in one of the most expensive crockery. The floor is installed with soft and beautifully textured carpet.")
        Game.jump(room.label + "_in")
        
label i_dining_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.prevNarrate = "What do you want to do?"
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit()
        
        if Game.input != "":
            try:
                room.do(Game.input)
            except:
                Game.narrateADV("I don't know what \"[Game.input]\" means.")
        
        Game.jump(room.label + "_in")
