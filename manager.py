import json
from character import Character


class Director:
    builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_character(self):
        character = Character()

        category = self.builder.get_category()
        character.category = category

        items = self.builder.get_items()
        character.items = items

        abilities = self.builder.get_abilities()
        character.abilities = abilities

        max_health = self.builder.get_max_health()
        character.max_health = max_health

        stats = self.builder.get_stats()
        character.stats = stats

        return character

class CharacterManager:
    _instance = None

    def __init__(self):
        self.character_storage_file_path = 'characters.json'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterManager, cls).__new__(cls)
        return cls._instance

    def load_character_by_index(self, index):
        characters = self.load_all_characters_from_file()
        return Character(**characters[index])

    def load_all_characters_from_file(self):
        try:
            with open(self.character_storage_file_path, 'r') as file:
                characters = json.load(file)
                return characters
        except:
            return []

    def change_character_name(self, character_index, new_name):
        character_for_update = self.load_character_by_index(character_index)
        character_for_update.set_name(new_name)

        self.update_character(character_index, character_for_update)

    def update_character(self, character_index, updated_character):
        self.delete_character(character_index)
        self.save_character(updated_character)

    def save_characters_to_file(self, characters):
        if len(characters):
            print("Saving characters to file...")
            with open(self.character_storage_file_path, 'w') as f:
                json.dump(characters, f, indent=2)
            print("Saved.")
        else:
            print('No characters created!')

    def obj_dict(obj):
        return obj.__dict__

    def save_character(self, character):
        character_list = self.load_all_characters_from_file()
        character_list.append(character) # append means add. In this case we load the characters that we already have and add a new character to the list
        with open(self.character_storage_file_path, 'w') as f:
            # 'default=lambda character: character.__dict__': while performing dump, we take every item inside
            # character_list, interpret it as 'character' and then take its __dict__ to dump into json
            # __dict__ basically returns all attributes of the object (for character class it's name, class, inventory, etc.)
            json.dump(character_list, f, default=lambda character: character.__dict__, indent=2)

    def delete_character(self, character_index):
        character_list = self.load_all_characters_from_file()
        character_list.pop(character_index)
        with open(self.character_storage_file_path, 'w') as f:
            json.dump(character_list, f, default=lambda character: character.__dict__, indent=2)

    def delete_character_item(self, character_index, item_index):
        character = self.load_character_by_index(character_index)
        character.get_items().pop(item_index)
        self.update_character(character_index, character)

    def add_new_character_item(self, character_index, new_item_name):
        character = self.load_character_by_index(character_index)
        character.get_items().append(new_item_name)
        self.update_character(character_index, character)

    def edit_character_stat(self, character_index, stat_name, new_stat_value):
        character = self.load_character_by_index(character_index)
        character.get_stats()[stat_name] = new_stat_value

        self.update_character(character_index, character)