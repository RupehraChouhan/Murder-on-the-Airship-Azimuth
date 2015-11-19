init -999 python: # Game class must be given first priority to load
    # Game is a purely static class, and does not need to be instantiated
    class Game:
        input = "" # Static(ish) variable player text input is put into
        __moves = 0 # Numbers of moves player has made
        notes = [] # List of states player has reached, for determining game progress and notebook entries
        
        # Get player input in ADV mode
        @staticmethod
        def inputADV(prompt):
            Game.input = renpy.input(prompt)
        
        # Get player input in NVL mode
        @staticmethod
        def inputNVL(prompt):
            Game.input = renpy.call_screen("nvl_input", prompt)
        
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
