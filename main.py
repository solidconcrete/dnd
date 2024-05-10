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


    characterManager = CharacterManager()
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

    def print_available_commands():
        print("Choose any of these commands:")
        for command in input_options.keys():
            print(f"{command} - {input_options[command]}")

    def get_user_input():
        return input("\nPlease enter a command: ")

    def start_warrior_creation():
        director.set_builder(warrior_builder)
        return director.getCharacter()

    def start_wizard_creation():
        director.set_builder(wizard_builder)
        return director.getCharacter()

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

    print_available_commands()

    while True:
        user_input = get_user_input()
        match user_input:
            case "h":
                print_available_commands()
            case "n":
                start_character_creation()
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
