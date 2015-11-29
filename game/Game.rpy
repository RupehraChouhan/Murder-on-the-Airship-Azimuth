init -999 python: # Game class must be given first priority to load
    # Game is a purely static class, and does not need to be instantiated
    class Game:
        input = "" # Static(ish) variable player text input is put into
        prevPrompt = "" # Stores the previous prompt from input
        prevNarrate = "" # Stores the previous narration from narrate
        __moves = 0 # Numbers of moves player has made
        __startTime = [0, 0]
        __moveTime = [0, 10]
        notes = [] # List of states player has reached, for determining game progress and notebook entries
        zeppelinName = "Azimuth"
        
        # Dictionary for tracking state
        state = {}
        
        # Dictionary for tracking clues
        # Name should be the one displayed
        cluesFound = {}

        # You as a speaker
        YOU = None
        
        # Array of npcs
        NPC_NUM = 7
        npcs = [None] * NPC_NUM
        NPC_KING = 0
        NPC_QUEEN = 1
        NPC_BISHOP = 2
        NPC_KNIGHT = 3
        NPC_ROOK = 4
        NPC_PAWN = 5
        NPC_CAPTAIN = 6
        
        # Array of rooms
        ROOM_NUM = 9
        rooms = [None] * ROOM_NUM
        ROOM_CABIN = 0
        ROOM_DINING = 1
        ROOM_GALLEY = 2
        ROOM_BATHS = 3
        ROOM_LOUNGE = 4
        ROOM_BAR = 5
        ROOM_CARGO = 6
        ROOM_COCKPIT = 7
        ROOM_ENGINE = 8
        
        MUSIC_INTRO = "audio/IntroMusic.ogg"
        
        # Narrator for narrating
        __NarratorADV = Character(None, kind=adv)
        __NarratorNVL = Character(None, kind=nvl)
        
        # Set the initial state of the game
        @staticmethod
        def initialize():
            # make a speaker for you
            Game.YOU = NPC("You", None, "#777777", [], alive=False) # 50% Grey, dead for all purposes

            # NPC defined in NPC.rpy
            Game.npcs[Game.NPC_KING] = NPC("King", None, "#ffffff", [], alive=False) # White, dead
            Game.npcs[Game.NPC_QUEEN] = NPC("Queen", "t_queen", "#ff0000", []) # Red
            Game.npcs[Game.NPC_BISHOP] = NPC("Bishop", "t_bishop", "#00ff00", []) # Green
            Game.npcs[Game.NPC_KNIGHT] = NPC("Knight", "t_knight", "#0000ff", []) # Blue
            Game.npcs[Game.NPC_ROOK] = NPC("Rook", "t_rook", "#ffff00", []) # Yellow
            Game.npcs[Game.NPC_PAWN] = NPC("Pawn", "t_pawn", "#00ffff", []) # Cyan
            Game.npcs[Game.NPC_CAPTAIN] = NPC("Captain", "t_captain", "#ff00ff", []) # Magenta
            
            # Room defined in Room.rpy
            Game.rooms[Game.ROOM_CABIN] = Room("Passenger Cabins", "i_cabin", 0, 0, ["Cabins", "Cabin"])
            Game.rooms[Game.ROOM_DINING] = Room("Dining Room", "i_dining", 1, 0, ["Dining"])
            Game.rooms[Game.ROOM_GALLEY] = Room("Galley", "i_galley", 2, 0, [])
            Game.rooms[Game.ROOM_BATHS] = Room("Baths", "i_baths", 0, 1, ["Bath"])
            Game.rooms[Game.ROOM_LOUNGE] = Room("Passenger Lounge", "i_lounge", 1, 1, ["Lounge"])
            Game.rooms[Game.ROOM_BAR] = Room("Bar", "i_bar", 2, 1, [])
            Game.rooms[Game.ROOM_CARGO] = Room("Cargo Hold", "i_cargo", 0, 2, ["Cargo", "Hold"])
            Game.rooms[Game.ROOM_COCKPIT] = Room("Cockpit", "i_cockpit", 1, 2, [])
            Game.rooms[Game.ROOM_ENGINE] = Room("Engine Room", "i_engine", 2, 2, ["Engine"])
        
        # Get player input in ADV mode
        # Several choices can be optionally added
        #   Each choice will display a number, and the string for the choice
        #   Input is received in the same way
        #   The user will expect number inputs, so PROCESS NUMBER STRINGS
        @staticmethod
        def inputADV(prompt, choices = [], forceValidNumber = False):
            endPrompt = prompt + "\n";
            
            if len(choices) > 0:
                for i in range(0,len(choices)):
                    endPrompt = endPrompt + "  " + str(i+1) + ". " + choices[i] + "\n"
                    
            Game.prevPrompt = endPrompt[:-1] # remove new line at end
            done = False
            while not done:
                Game.input = renpy.input(endPrompt)
                
                if forceValidNumber:
                    try:
                        num = int(Game.input)
                        if num > 0 and num <= len(choices):
                            done = True
                        else:
                            raise Error()
                    except:
                        Game.narrateADV("I don't know what you mean.")
                else:
                    done = True
        
        # Get player input in NVL mode
        # Several choices can be optionally added
        #   Each choice will display a number, and the string for the choice
        #   Input is received in the same way
        #   The user will expect number inputs, so PROCESS NUMBER STRINGS
        @staticmethod
        def inputNVL(prompt, choices = [], forceValidNumber = False):
            endPrompt = prompt + "\n";
            
            if len(choices) > 0:
                for i in range(0,len(choices)):
                    endPrompt = endPrompt + "  " + str(i+1) + ". " + choices[i] + "\n"
                    
            Game.prevPrompt = endPrompt[:-1] # remove newline at end
            done = False
            while not done:
                Game.input = renpy.call_screen("nvl_input", endPrompt)
                
                if forceValidNumber:
                    try:
                        num = int(Game.input)
                        if num > 0 and num <= len(choices):
                            done = True
                        else:
                            raise Error()
                    except:
                        Game.narrateNVL("I don't know what you mean.")
                else:
                    done = True
            
        
        # Facade method for jumping to labels in Ren'Py, if anything needs to be done every jump it can be done here
        @staticmethod
        def jump(label):
            renpy.jump(label)
        
        # Automatically check last player input against predetermined quit commands, and jump to label if one matches
        # Default label is the start menu of the game
        @staticmethod
        def checkQuit(label="start"):
            target = Game.input.lower()
            if target == "q": Game.jump(label)
            if target == "quit": Game.jump(label)
            if target == "e": Game.jump(label)
            if target == "exit": Game.jump(label)
            
        # Increment the number of moves, and check if anything needs to happen
        @staticmethod
        def incrementMoves():
            Game.__moves += 1
            # checks would be done here
            
        @staticmethod
        def getMoves():
            return Game.__moves
            
        @staticmethod
        def narrateADV(line):
            Game.prevNarrate = line
            renpy.say(Game.__NarratorADV, line)
        
        @staticmethod
        def narrateNVL(line):
            Game.prevNarrate = line
            renpy.say(Game.__NarratorNVL, line)
            
        # return the time as a pair [hour, minutes]
        @staticmethod
        def time():
            time = [0, 0]
            # calc hours
            time[0] = (Game.__startTime[0] + time[0] + (moves * Game.__moveTime[0]) + (moves * Game.__moveTime[1] // 60) ) % 24
            # calc minutes
            time[1] = Game.__startTime[1] + time[1] + (moves * Game.__moveTime[1] % 60)
            
            return time
            
        # return the time as a string
        @staticmethod
        def timeString():
            time = Game.time()
            return "{hours:02d}:{minutes:02d}".format(hours=time[0], minutes=time[1])
    
# initialize the game state after other classes
init -997 python:
    Game.initialize()