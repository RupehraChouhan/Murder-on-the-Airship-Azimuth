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
    
    class NPC:
        def __init__(self, name, color):
            self.name = name
            self.npc = Character(name, kind=nvl, color=color)
    
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

label investigate_room:
    python:
        input = renpy.input("What room do you want to investigate?")
        action = -1
        destination = ""
        for x in room:
            if input.lower() == x.name.lower():
                destination = input
                action = 1
        if checkQuit(input.lower()):
            action = 0
    
    if action == 1:
        jump room_found
    if action == 0:
        jump starting_hub
    
    "I don't know what [input] means."
    jump investigate_room
    
label room_found:
    python:
        input = renpy.input("Here we are in the [destination]! What a big room.")
        action = -1
        if checkQuit(input.lower()):
            action = 0
    
    if action == 0:
        jump starting_hub
    
    "I don't know what [input] means."
    jump room_found

label talk_suspect:

    jump starting_hub

label look_notepad:

    jump starting_hub

label solve_case:

    jump starting_hub
