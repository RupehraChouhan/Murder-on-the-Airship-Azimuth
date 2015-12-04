init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_COCKPIT]
    
    def look():
        Game.narrateADV("The door to the cockpit is locked, as it always is during flight, but you can see in through its glass back wall.")
        Game.prevNarrate = "The cockpit is filled with lights and mechanical gizmos. Captain Elizabeth Winfarthing is maneuvering expertly among the controls. You are in good hands, up here."
    room.addCommand("look", look)

    # clean up namespace
    del look
    
label i_cockpit:
    scene bg cockPitImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_COCKPIT]
        
        # Opening description of the room
        Game.narrateADV("This room is a glass-walled observation deck overlooking the darkened countryside. It also overlooks the sunken cockpit where Captain Winfarthing and her crew bustle about.")
        Game.prevNarrate = "She is an expert and has been working for Royaume & Sons for a long time. You trust her to fly you safely to Endsville."
        Game.jump(room.label + "_in")
        
label i_cockpit_in:        
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
