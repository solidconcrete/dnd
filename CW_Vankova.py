import json

class CharacterFactory:
    def create_character(self):
        name = input("Enter character name: ")
        character_class = input("Enter character class: ")
        history = input("Enter character history: ")
        return Character(name, character_class, history)

class Character:
    def __init__(self, name, character_class, history):
        self.name = name
        self.character_class = character_class
        self.history = history
        self.stats = {}
        self.health = 100
        self.inventory = []
        self.abilities = []

    def set_stats(self):
        print("Enter character statistics:")
        self.stats['STR'] = int(input("Strength: "))
        self.stats['DEX'] = int(input("Dexterity: "))
        self.stats['CON'] = int(input("Constitution: "))
        self.stats['INT'] = int(input("Intelligence: "))
        self.stats['WIS'] = int(input("Wisdom: "))
        self.stats['CHA'] = int(input("Charisma: "))

    def add_to_inventory(self):
        item = input("Enter an item to add to inventory (or leave blank to stop): ")
        while item:
            self.inventory.append(item)
            item = input("Enter another item to add to inventory (or leave blank to stop): ")

    def add_ability(self):
        ability = input("Enter an ability to add (or leave blank to stop): ")
        while ability:
            self.abilities.append(ability)
            ability = input("Enter another ability to add (or leave blank to stop): ")

    def to_dict(self):
        return {
            'name': self.name,
            'class': self.character_class,
            'history': self.history,
            'stats': self.stats,
            'health': self.health,
            'inventory': self.inventory,
            'abilities': self.abilities
        }

class CharacterManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterManager, cls).__new__(cls)
            cls.characters = []
        return cls._instance

    def add_character(self, character):
        self.characters.append(character)

    def clear_characters(self):
        self.characters = []

    def save_characters_to_file(self, filename):
        with open(filename, 'a') as file:  # Use 'a' mode for appending
            for character in self.characters:
                json.dump(character.to_dict(), file)
                file.write('\n')  # Separate character data with a newline

    def load_characters_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                char_data = json.loads(line.strip())
                self.characters.append(Character(**char_data))

# Example usage:
if __name__ == "__main__":
    factory = CharacterFactory()

    # Create and manage characters
    character_manager = CharacterManager()

    # Add characters
    num_characters = int(input("Enter the number of characters to create: "))
    for _ in range(num_characters):
        character = factory.create_character()
        character.set_stats()
        character.add_to_inventory()
        character.add_ability()
        character_manager.add_character(character)

    characters_file = "characters.json"
    # Save characters to file
    character_manager.save_characters_to_file(characters_file)

    # Load characters from file
    character_manager.clear_characters()  # Clear existing characters
    character_manager.load_characters_from_file(characters_file)

    # Print loaded characters
    print("Characters loaded from file:")
    for character in character_manager.characters:
        print(character.name)