init -998 python: # Other classes are given first priority to load, after Game class
    class Room:
        # Default matching strings is an empty list
        def __init__(self, name, label, x, y, matches=[]):
            self.name = name # Name of Room
            self.label = label # Label to jump to to begin inspection, cannot be None
            self.x = x # x-coordinate of Room in spatial layout
            self.y = y # y-coordinate of Room in spatial layout
            
            self.matches = [] # List of strings that can be used to match this Room
            if name: # Name only included if given one
                self.matches += [name.lower()]
            for m in matches:
                self.matches += [m.lower()]
        
        # Returns true if target matches any allowed string for this Room
        def match(self, target):
            target = target.lower()
            for m in self.matches:
                if target == m:
                    return True
            return False
