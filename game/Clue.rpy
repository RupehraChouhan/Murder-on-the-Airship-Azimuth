init -998 python:
    class Clue:
        def __init__(self, name, commands, functions):
            self.name = name
            self.functions = {}
            
            for i in range(0,len(commands)):
                self.functions[commands[i]] = functions[i]
            
        def do(self, command):
            self.functions[command]()
        
        
