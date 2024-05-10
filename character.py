def validate_stat_input(func):
    def wrapper(self, stat_name, value):
        if not isinstance(stat_name, str) or not isinstance(value, int):
            raise ValueError("Invalid input: stat_name must be a string and value must be an integer.")
        return func(self, stat_name, value)
    return wrapper

def validate_stat_values(func):
    def wrapper(self, stat_name, value):
        while value < 0 or value > 20:
            print("Invalid value. Stat values must be between 0 and 20.")
            value = int(input("Enter the new value for {}: ".format(stat_name)))
        return func(self, stat_name, value)
    return wrapper

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
    @validate_stat_values
    def set_stat(self, stat_name, value):
        self.character['stats'][stat_name] = value

    def add_ability(self, ability):
        self.character['abilities'].append(ability)

    def remove_ability(self, ability):
        self.character['abilities'].remove(ability)

    def add_item_to_inventory(self, item):
        self.character['inventory'].append(item)

    def remove_item_from_inventory(self, item):
        self.character['inventory'].remove(item)