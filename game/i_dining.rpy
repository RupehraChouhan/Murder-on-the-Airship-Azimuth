init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_DINING]
    Game.cluesFound[Game.DINING_SPECTACLES] = False
    
    def look():
        Game.inputADV( "These glasses appear to belong to the bishop *changeme*" )
        Game.cluesFound[Game.DINING_SPECTACLES] = True
    glasses = Clue( "glasses", [ "look" ], [ look ] )

label i_dining:
    scene bg diningImage
    with fade
    stop music fadeout 2

    python:
        room = Game.rooms[Game.ROOM_DINING]
        Game.narrateADV("Here we are in the [room.name] where everyone had supper at 7pm. The king was last seen alive here.")
        Game.narrateADV("Dining is a massive room with big windows on the side providing a very beautiful view of the outside.")
        Game.narrateADV("The dining tables are covered with graceful white cloth where the passengers are served in one of the most expensive crockery. The floor is installed with soft and beautifully textured carpet. ")
        Game.inputADV("What do you want to do?")
        Game.jump(room.label + "_in")
        
label i_dining_in:        
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
