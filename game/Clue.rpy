init -998 python:
    class Clue:
        def __init__(self, name, commands, functions):
            self.name = name
            self.commands = commands
            self.functions = functions
            
        def do(self, command):
            for i in range(0,len(self.commands)):
                if self.commands[i] == command:
                    self.functions[i]()
        
        
