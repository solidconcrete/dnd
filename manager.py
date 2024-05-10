import json
from character import Character


class CharacterManager:
    _instance = None

    def __init__(self):
        # self.characters = None
        self.character_storage_file_path = 'characters.json'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterManager, cls).__new__(cls)
            # load_characters_from_file(th)
        return cls._instance

    def load_character_by_index(self, index):
        characters = self.load_all_characters_from_file()
        return Character(**characters[index])

    def load_all_characters_from_file(self):
        try:
            with open(self.character_storage_file_path, 'r') as file:
                characters = json.load(file)
                return characters
        except FileNotFoundError:
            return []

    def change_character_name(self, character_index, new_character_name):
        character = self.load_character_by_index(character_index)
        self.delete_character(character_index)

        character.set_name(new_character_name)

        character.set_name(new_character_name)
        self.save_character(character)

    def update_character(self, character_index, updated_character):
        all_characters = self.load_all_characters_from_file()

        all_characters.pop(character_index)

        self.save_character(updated_character)
        # except FileNotFoundError:
        #     print("Character file not found. Starting with an empty list.")
        # except json.JSONDecodeError:
        #     print("Error decoding JSON. Starting with an empty list.")

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
            # json.dump(character.__dict__, f, indent=2)
        # with open(self.character_storage_file_path, 'w') as f:
        #     json.dumps(character)

    def delete_character(self, character_index):
        character_list = self.load_all_characters_from_file()
        character_list.pop(character_index)
        with open(self.character_storage_file_path, 'w') as f:
            json.dump(character_list, f, default=lambda character: character.__dict__, indent=2)

    # def edit_character(self, character_name):
    #     print(f"Attempting to edit character: {character_name}")
    #     for character_dict in self.characters:
    #         if character_dict['name'] == character_name:
    #             print("Editing character:", character_dict['name'])
    #             print("1. Edit history")
    #             print("2. Edit class")
    #             print("3. Edit statistics")
    #             print("4. Edit abilities")
    #             print("5. Edit inventory")
    #             choice = input("Enter your choice: ")
    #             if choice == "1":
    #                 character_dict['history'] = input("Enter updated character history: ")
    #             elif choice == "2":
    #                 character_dict['class'] = input("Enter updated character class: ")
    #             elif choice == "3":
    #                 stat_name = input("Enter the stat to edit (e.g., STR, DEX): ")
    #                 value = int(input(f"Enter the new value for {stat_name}: "))
    #                 character = Character()
    #                 character.character = character_dict
    #                 character.set_stat(stat_name, value)
    #             elif choice == "4":
    #                 self.edit_abilities(character_dict)
    #             elif choice == "5":
    #                 self.edit_inventory(character_dict)
    #             else:
    #                 print("Invalid choice.")
    #             return
    #     print("Character not found.")

    # def edit_abilities(self, character):
    #     print("Current abilities:", character['abilities'])
    #     print("1. Add ability")
    #     print("2. Remove ability")
    #     choice = input("Enter your choice: ")
    #     if choice == "1":
    #         new_ability = input("Enter new ability: ")
    #         character['abilities'].append(new_ability)
    #     elif choice == "2":
    #         ability_to_remove = input("Enter ability to remove: ")
    #         if ability_to_remove in character['abilities']:
    #             character['abilities'].remove(ability_to_remove)
    #         else:
    #             print("Ability not found.")
    #     else:
    #         print("Invalid choice.")

    # def edit_inventory(self, character):
    #     print("Current inventory:", character['inventory'])
    #     print("1. Add item")
    #     print("2. Remove item")
    #     choice = input("Enter your choice: ")
    #     if choice == "1":
    #         new_item = input("Enter new item: ")
    #         character['inventory'].append(new_item)
    #     elif choice == "2":
    #         item_to_remove = input("Enter item to remove: ")
    #         if item_to_remove in character['inventory']:
    #             character['inventory'].remove(item_to_remove)
    #         else:
    #             print("Item not found.")
    #     else:
    #         print("Invalid choice.")