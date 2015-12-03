init 0 python: # set up clues and commands in room
    room = Game.rooms[Game.ROOM_COCKPIT]
    
    def look():
        Game.prevNarrate = "The cockpit is filled with lights and mechanical gizmos. Captain Elizabeth Winfarthing is maneuvering expertly among the controls. You are in good hands, up here."
    room.addCommand("look", look)

label i_cockpit:
    scene bg cockPitImage
    with fade

    python:
        # The room you are in
        room = Game.rooms[Game.ROOM_COCKPIT]
        
        # Opening description of the room
        Game.narrateADV("Here in the cockpit meet the captain Elizabeth. She is an expert and has been working for the king for a long time. We trust her for flying us safely to Endsville.")
        Game.prevNarrate = "What do you want to do?"
        Game.jump(room.label + "_in")
        
label i_cockpit_in:        
    python:
        # assumption: if all functions of clues are narrateADV, then we can loop through this
        Game.inputADV( Game.prevNarrate )
        Game.checkQuit(room.label + "_in")
        
        try:
            room.do(Game.input)
        except:
            temp = Game.prevNarrate
            Game.narrateADV("I don't know what \"[Game.input]\" means.")
            Game.prevNarrate = temp
        
        Game.jump(room.label + "_in")
