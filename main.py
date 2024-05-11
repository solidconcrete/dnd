import os

from character import Character, WarriorBuilder, WizardBuilder
from manager import CharacterManager

if __name__ == "__main__":
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

    character_manager = CharacterManager()
    warrior_builder = WarriorBuilder()
    wizard_builder = WizardBuilder()
    director = Director()

    print("Welcome to DND character manager, what would you like to do?")
    input_options = {
        "l": "List all characters",
        "n": "Create new character",
        "e": "Edit character",
        "h": "Help (display available commands)",
        "q": "Quit"
    }

    character_edit_options = {
        "0": "Delete character",
        "1": "Edit name",
        "2": "Edit backstory",
        "3": "Edit class",
        "4": "Edit items",
        "5": "Edit abilities",
        "6": "Edit stats",
        "7": "Edit max health",
    }

    def print_available_commands():
        print("Choose any of these commands:")
        for command in input_options.keys():
            print(f"{command} - {input_options[command]}")

    def print_available_character_edit_commands():
        print("Choose any of these commands:")
        for command in character_edit_options.keys():
            print(f"{command} - {character_edit_options[command]}")

    def get_user_input():
        return input("\nPlease enter a command: ")

    def start_warrior_creation():
        director.set_builder(warrior_builder)
        return director.build_character()

    def start_wizard_creation():
        director.set_builder(wizard_builder)
        return director.build_character()

    def ask_confirmation(prompt):
        result = input(prompt)
        if result == "Y" or result == "y":
            return True                         # if user replied Y, then we exit from this function by using 'return'
        if result == "N" or result == "n":
            return False                        # if user replied N, then we exit from this function by using 'return'
        ask_confirmation(prompt)                # if user's answer was neither Y or N (maybe he made a typo), then repeat this function

    def start_character_creation():
        user_input = input("\nChoose the class of your character: Warrior (1) or Wizard(2): ")
        match user_input:
            case "1":
                character = start_warrior_creation()
            case "2":
                character = start_wizard_creation()
            case _:
                print("Invalid input")
                return

        character.set_name(input("Enter character's name: "))
        character.set_back_story(input("Enter character's backstory: "))

        print("\nCharacter has been created. Here are their stats: ")
        print(character.display_info())

        save_changes = ask_confirmation("Apply changes (Y/N)? ")
        # if function ask_confirmation returned True, then we save the character, otherwise the function just ends without saving
        if save_changes == True:
            character_manager.save_character(character)

    def start_character_deletion(character_index):
        delete = ask_confirmation("Are you sure that you want to delete this character?")
        if delete == True:
            character_manager.delete_character(character_index)


    def start_items_edit(character_index):
        character = character_manager.load_character_by_index(character_index)

        print("Selected character has following items: ")
        for i, item in enumerate(character.items):
            print(f"{i}. {item}")

        action = input("Do you want to remove (0) or add (1) an item? ")
        match action:
            case "0":
                item_index = input("Choose item to delete by typing its number")
                character_manager.delete_character_item(character_index, int(item_index))
            case "1":
                new_item_name = input("Which item would you like to add? Type new Item name")
                character_manager.add_new_character_item(character_index, new_item_name)

    def validate_stat(stat_value):
        return 0 < int(stat_value) <= 20

    def get_stat_name_by_index(character, stat_index):
        for i, stat in enumerate(character.stats):
            if i == int(stat_index):
                return stat

    def start_stats_edit(character_index):
        character = character_manager.load_character_by_index(character_index)
        print("Selected character has following stats: ")
        for i, stat in enumerate(character.stats):
            print(f"{i}. {stat}: {character.stats[stat]}")

        stat_to_edit_index = input("\nChoose a stat to edit by typing its number: ")

        new_stat_value = int(input("Enter new stat value: "))
        stat_name = get_stat_name_by_index(character, stat_to_edit_index)

        if not validate_stat(new_stat_value):
            print("\nInvalid stat value. Value must be between 1 and 20.")
            start_stats_edit(character_index)

        character_manager.edit_character_stat(character_index, stat_name, new_stat_value)

    def start_character_edit():
        character_index = input("\nChoose character to edit by typing their number ")
        character_index = int(character_index) # convert user's input from text to number format using int()

        # Since 'load_character_by_index' returns character as object, in order to display it in human-readable manner,
        # we call __dict__, which outputs its parameters (name, class, stats, etc.)
        print(character_manager.load_character_by_index(character_index).__dict__)
        user_action = input(print_available_character_edit_commands())

        match user_action:
            case "0":
                start_character_deletion(character_index)
            case "1":
                start_character_name_edit(character_index)
            case "2":
                pass # TODO: the same as name edit
            case "3":
                pass  # TODO: the same as name edit
            case "4":
                start_items_edit(character_index)
            case "5":
                pass # TODO
            case "6":
                start_stats_edit(character_index)
            case _:
                print("Unknown command. Type 'h' to see the list of available commands.")


    def start_character_name_edit(character_index):
        new_name = input("Enter new character's name: ")
        character_manager.change_character_name(character_index, new_name)

    def start_character_class_edit(character_index):
        pass # TODO

    print_available_commands()

    while True:
        user_input = get_user_input()
        match user_input:
            case "h":
                print_available_commands()
            case "n":
                start_character_creation()
            case "l":
                characters_from_storage = character_manager.load_all_characters_from_file()
                for i, character in enumerate(characters_from_storage):
                    print(f"{i}. {character}")
            case "e":
                start_character_edit()
            case "q":
                print("\nBye :)\n")
                quit()
                break
            case _:
                print("Unknown command. Type 'h' to see the list of available commands.")
    # while True:
    #     choice = get_string_choice(prompt, **input_options)
    #     match choice:
    #         case "c":
    #             name = input("Enter character name: ")
    #             character_class = input("Enter character class: ")
    #             history = input("Enter character history: ")
    #
    #             char = Character()
    #             char.create_char(name, character_class, history)
    #
    #             # Add character dictionary to characters list of CharacterManager class
    #             characterManager.add_character(char.character)
    #             print("Character created.\n")
    #
    #         case "l":
    #             if len(characterManager.characters):
    #                 for u in characterManager.characters:
    #                     print(u['name'])
    #                 print('\n\n')
    #             else:
    #                 print("No characters created yet.\n")
    #
    #         case "e":
    #             character_name = input("Enter the name of the character to edit: ")
    #             characterManager.edit_character(character_name)
    #
    #         case "s":
    #             characterManager.save_characters_to_file()
    #
    #         case "q":
    #             print("\nBye :)\n")
    #             quit()
    #             break
    #
    #         case _:
    #             print("Invalid choice. Please select a valid option.\n")
    #
    #
    #     # Validate user choices and return it as a string if it's correct
    #     def get_string_choice(prompt, **kwoptions):
    #         while True:
    #             try:
    #                 print(prompt)
    #
    #                 # Loop through kwoptions and print them
    #                 for key, value in kwoptions.items():
    #                     print("{0} = {1}".format(key, value))
    #
    #                 user_choice = input()
    #                 if user_choice in kwoptions:
    #                     return user_choice
    #
    #                 # Error in case choice is not in kwoption
    #                 print("That wasn't one of the options")
    #             except TypeError:
    #                 # Throw exception incase user input has invalid type
    #                 print("\n\n")
    #                 raise TypeError
