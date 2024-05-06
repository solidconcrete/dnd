from character import Character
from manager import CharacterManager
import json
import sys

 # Validate user choices and return it as a string if it's correct
def get_string_choice(prompt, **kwoptions):
    while True:
        try:
            print(prompt)
            
            # Loop through kwoptions and print them
            for key, value in kwoptions.items():
                print("{0} = {1}".format(key, value))
            
            user_choice = input()
            if user_choice in kwoptions:
                return user_choice
            
            # Error in case choice is not in kwoption
            print("That wasn't one of the options")
        except TypeError:
            # Throw exception incase user input has invalid type
            print("\n\n")
            raise TypeError


if __name__ == "__main__":

    char_manager = CharacterManager() 

    prompt = "Welcome to DND manager, what would you like to do?"
    input_options = {
            "c": "Create character",
            "l": "List created characters",
            "e": "Edit character",
            "s": "Save character/s",
            "q": "Quit"
    }
    
    while True:
        choice = get_string_choice(prompt, **input_options)
        match choice:
            case "c":
                
                name = input("Enter character name: ")
                character_class = input("Enter character class: ")
                history = input("Enter character history: ")
                
                char = Character()
                char.create_char(name, character_class, history)
                
                # Add character dictionary to characters list of CharacterManager class
                char_manager.add_character(char.character)
                print("Character created.\n")
                
                #TODO return to choice prompt
            case "l":
                if len(char_manager.characters):
                    for u in char_manager.characters:
                        print(u['name'])
                    print('\n\n')
            case "e":
                character_name = input("Enter the name of the character to edit: ")
                char_manager.edit_character()
            
            case "s":
                char_manager.save_characters_to_file()
            
            case "q":
                print("\nBye :)\n")
                quit()
                break
            
            case _:
                print("Invalid choice. Please select a valid option.\n")
                break 
   

