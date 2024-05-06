from decorators import validate_stat_input
class Character:
    def __init__(self):
        self.character = {}
        
        self.character['health'] = 100       # Set default health to 100
        self.character['stats'] = {}         # Empty dict for stats, can be filled only during editing
        self.character['inventory'] = []     # Empty list for inventory, can be filled only during editing
        self.character['abilities'] = []     # Empty list for abilities, can be filled only during editing

    def create_char(self, name, character_class, history):
        self.character['name'] = name
        self.character['class'] = character_class
        self.character['history'] = history
        
    @validate_stat_input
    def set_stat(self, stat_name, value):
        self.character['stats'][stat_name] = value
