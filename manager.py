import json

class CharacterManager:
    _instance = None

    def __init__(self):
        self.characters = None
        self.character_storage_file_path = './character_storage.json'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterManager, cls).__new__(cls)
            # load_characters_from_file(th)
        return cls._instance

    def load_characters_from_file(self):
        try:
            with open(self.character_storage_file_path, 'r') as file:
                self.characters = json.load(file)
                print(f"Loaded characters: {self.characters}")
        except FileNotFoundError:
            print("Character file not found. Starting with an empty list.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty list.")

    def add_character(self, character):
        self.characters.append(character)

    def clear_characters(self):
        self.characters = []

    def save_characters_to_file(self):
        if len(self.characters):
            print("Saving characters to file...")
            with open(self.char_file, 'w') as f:
                json.dump(self.characters, f, indent=2)
            print("Saved.")
        else:
            print('No characters created!')
    
    def edit_character(self, character_name):
        print(f"Attempting to edit character: {character_name}")
        for character_dict in self.characters:
            if character_dict['name'] == character_name:
                print("Editing character:", character_dict['name'])
                print("1. Edit history")
                print("2. Edit class")
                print("3. Edit statistics")
                print("4. Edit abilities")
                print("5. Edit inventory")
                choice = input("Enter your choice: ")
                if choice == "1":
                    character_dict['history'] = input("Enter updated character history: ")
                elif choice == "2":
                    character_dict['class'] = input("Enter updated character class: ")
                elif choice == "3":
                    stat_name = input("Enter the stat to edit (e.g., STR, DEX): ")
                    value = int(input(f"Enter the new value for {stat_name}: "))
                    character = Character()
                    character.character = character_dict
                    character.set_stat(stat_name, value)
                elif choice == "4":
                    self.edit_abilities(character_dict)
                elif choice == "5":
                    self.edit_inventory(character_dict)
                else:
                    print("Invalid choice.")
                return
        print("Character not found.")

    def edit_abilities(self, character):
        print("Current abilities:", character['abilities'])
        print("1. Add ability")
        print("2. Remove ability")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_ability = input("Enter new ability: ")
            character['abilities'].append(new_ability)
        elif choice == "2":
            ability_to_remove = input("Enter ability to remove: ")
            if ability_to_remove in character['abilities']:
                character['abilities'].remove(ability_to_remove)
            else:
                print("Ability not found.")
        else:
            print("Invalid choice.")

    def edit_inventory(self, character):
        print("Current inventory:", character['inventory'])
        print("1. Add item")
        print("2. Remove item")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_item = input("Enter new item: ")
            character['inventory'].append(new_item)
        elif choice == "2":
            item_to_remove = input("Enter item to remove: ")
            if item_to_remove in character['inventory']:
                character['inventory'].remove(item_to_remove)
            else:
                print("Item not found.")
        else:
            print("Invalid choice.")