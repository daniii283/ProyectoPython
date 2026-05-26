class CommandRegistry:
    def __init__(self):
        self._commands = {}
    
    def register(self, name, description, handler):
        self._commands[name] = {
            "description": description,
            "handler": handler
        }
        
    def get(self, name):
        return self._commands.get(name)
    
    def all(self):
        return self._commands.items()