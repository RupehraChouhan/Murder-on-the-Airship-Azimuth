init -999 python: # Game class must be given first priority to load
    class Game:
        input = "" # Static(ish) variable player text input is put into
        
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
        # Default label is the start of the game
        @staticmethod
        def checkQuit(label="start"):
            target = Game.input.lower()
            if target == "q": Game.jump(label)
            if target == "quit": Game.jump(label)
            if target == "e": Game.jump(label)
            if target == "exit": Game.jump(label)
