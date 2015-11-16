label investigate_room:
    python:
        input = renpy.input("What room do you want to investigate?")
        action = -1
        destination = ""
        for x in room:
            if input.lower() == x.name.lower():
                destination = input
                action = 1
                break
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
