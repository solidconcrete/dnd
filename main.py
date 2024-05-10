import os

from character import Character, WarriorBuilder, WizardBuilder
from manager import CharacterManager

if __name__ == "__main__":
    class Director:
        builder = None

        def set_builder(self, builder):
            self.builder = builder

        def getCharacter(self):
            character = Character()

            category = self.builder.get_category()
            character.category = category

            items = self.builder.get_items()
            character.items = items

            abilities = self.builder.get_abilities()
            character.abilities = abilities

            max_health = self.builder.get_max_health()
            character.max_health = max_health

            return character

    character_manager = CharacterManager()
    warrior_builder = WarriorBuilder()
    wizard_builder = WizardBuilder()
    director = Director()

    print("Welcome to DND character manager, what would you like to do?")
    input_options = {
        "c": "Create character",
        "l": "List all characters",
        "n": "Create new character",
        "s": "Select character",
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
        "6": "Edit max health",
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
        return director.getCharacter()

    def start_wizard_creation():
        director.set_builder(wizard_builder)
        return director.getCharacter()

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

        # if user answered Y, then we save the character, in any other case the function just ends without saving
        if save_changes == True:
            character_manager.save_character(character)


    def start_character_edit():
        user_input = input("\nChoose character to edit by typing their number ")
        print(character_manager.load_character_by_index(int(user_input)))
        print(print_available_character_edit_commands())

    def start_character_name_edit(character_index):
        new_name = input("Enter new character's name: ")
        character_manager.change_character_name(character_index, new_name)

    print_available_commands()

    while True:
        user_input = get_user_input()
        match user_input:
            case "h":
                print_available_commands()
            case "n":
                start_character_creation()
            case "l":
                characters_from_storage = character_manager.load_characters_from_file()
                for i, character in enumerate(characters_from_storage):
                    print(f"{i}. {character}")
            case "e":
                start_character_edit()
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
