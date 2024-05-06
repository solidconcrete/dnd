import json
class CharacterManager:
    _instance = None
    
    def __init__(self):
        self.char_file = "./characters.json"
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterManager, cls).__new__(cls)
            cls.characters = []
        return cls._instance

    def add_character(self, character):
        self.characters.append(character)

    def clear_characters(self):
        self.characters = []

    def save_characters_to_file(self):
        if len(self.characters):
            print("Saving characters to file...")
            
            f = open(self.char_file, 'a')
            try:
                json.dump(self.characters, f, indent=2)
            finally:
                f.close()
                print("Saved.")
        else:
            print('No characters created!')
        

    def load_characters_from_file(self):
        with open(self.char_file, 'r') as file:
            for line in file:
                char_data = json.loads(line.strip())
                self.characters.append(char_data)

    def edit_character(self, character_name):
        for character in self.characters:
            if character.name == character_name:
                print("Editing character:", character.name)
                print("1. Edit history")
                print("2. Edit class")
                print("3. Edit statistics")
                print("4. Edit abilities")
                choice = input("Enter your choice: ")
                if choice == "1":
                    character.history = input("Enter updated character history: ")
                elif choice == "2":
                    character.character_class = input("Enter updated character class: ")
                elif choice == "3":
                    stat_name = input("Enter the stat to edit (e.g., STR, DEX): ")
                    value = int(input("Enter the new value for {}: ".format(stat_name)))
                    character.set_stat(stat_name, value)
                elif choice == "4":
                    print("Current character abilities:", character.abilities)
                    index = int(input("Enter the index of the ability to edit (starting from 0): "))
                    if 0 <= index < len(character.abilities):
                        new_ability = input("Enter the updated ability: ")
                        character.abilities[index] = new_ability
                    else:
                        print("Invalid index.")
                else:
                    print("Invalid choice.")
                return
        print("Character not found.")
