init python:
    # Change to nvl, fullscreen text mode
    menu = nvl_menu
    narrator = Character(None, kind=nvl)
    
    # Automatically check player input against predetermined quit commands
    def checkQuit(input):
        if input == "q": return True
        if input == "quit": return True
        if input == "e": return True
        if input == "exit": return True
        return False
    
    # Array of NPCs
    npc = [NPC("King", "#ffffff"), # White
           NPC("Queen", "#ff0000"), # Red
           NPC("Bishop", "#00ff00"), # Green
           NPC("Knight", "#0000ff"), # Blue
           NPC("Rook", "#ffff00"), # Yellow
           NPC("Pawn", "#00ffff")] # Cyan
    
    class Room:
        def __init__(self, name, x, y):
            self.name = name
            self.x = x
            self.y = y
    
    # Array of rooms
    room = [Room("Passenger Cabins", 0, 0),
            Room("Dining Room", 1, 0),
            Room("Galley", 2, 0),
            Room("Baths", 0, 1),
            Room("Passenger Lounge", 1, 1),
            Room("Bar", 2, 1),
            Room("Cargo Hold", 0, 2),
            Room("Cockpit", 1, 2),
            Room("Engine Room", 2, 2)]

# The game starts here.
label start:

label starting_hub: # Jump here to go back to the selection menu
menu:
    "Investigate a room.":
        jump investigate_room
    "Talk to a suspect.":
        jump talk_suspect
    "Look at your notepad.":
        jump look_notepad
    "Solve the case.":
        jump solve_case

label talk_suspect:
    npc[0].npc "Hello World!"
    python:
        action = -1
        input = renpy.input("")
        if checkQuit(input.lower()):
            action = 0
    
    if action == 0:
        jump starting_hub
    else:
        npc[0].npc "[input]"
    
    jump starting_hub

label look_notepad:

    jump starting_hub

label solve_case:

    jump starting_hub
