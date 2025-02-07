# def validate_stat_input(func):
#     def wrapper(self, stat_name, value):
#         if not isinstance(stat_name, str) or not isinstance(value, int):
#             raise ValueError("Invalid input: stat_name must be a string and value must be an integer.")
#         return func(self, stat_name, value)
#     return wrapper
#
# def validate_stat_values(func):
#     def wrapper(self, stat_name, value):
#         while value < 0 or value > 20:
#             print("Invalid value. Stat values must be between 0 and 20.")
#             value = int(input("Enter the new value for {}: ".format(stat_name)))
#         return func(self, stat_name, value)
#     return wrapper
import json


# done using https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_builder.htm
# class Director:
#     builder = None
#
#     def setBuilder(self, builder):
#         self.builder = builder
#
#     def getCharacter(self):
#         character = Character()
#
#         category = self.builder.getCategory()
#         character.character = category
#
#         items = self.builder.getItems()
#         character.items = items
#
#         abilities = self.builder.getAbilities()
#         character.abilities = abilities
#
#         max_health = self.builder.getMaxHealth()
#         character.max_health = max_health
#
#         return character

class Character(object):
    def __init__(self, name=None, backstory=None, category=None, items=None, abilities=None, max_health=None, stats=None):
        self.name = name
        self.backstory = backstory
        self.category = category  # the word 'class' is a reserved keyword, so the solution is to use the word 'category'
        self.items = items
        self.abilities = abilities
        self.max_health = max_health
        self.stats = stats

    def set_name(self, name):
        self.name = name

    def set_back_story(self, back_story):
        self.backstory = back_story

    def get_stats(self):
        return self.stats

    def display_info(self):
        print("Name: ", self.name)
        print("Class: ", self.category)
        print("Max Health: ", self.max_health)
        print("Backstory: ", self.backstory)
        print("Inventory: ", self.items)
        print("Abilities: ", self.abilities)
        print("Stats: ", self.stats)

class CharacterBuilder:
    def get_name(self):
        pass

    def get_backstory(self):
        pass

    def get_category(self):
        pass

    def get_items(self):
        pass

    def get_abilities(self):
        pass

    def get_max_health(self):
        pass

    def get_stats(self):
        pass


# Concrete builder
class WarriorBuilder(CharacterBuilder):
    def get_category(self):
        return "Warrior"

    def get_items(self):
        return ["Axe", "Chainmail", "Helmet", "Testosterone"]

    def get_abilities(self):
        return ["Berserk", "Impenetrable", "Permanent hangover"]

    def get_max_health(self):
        return 300

    def get_stats(self):
        stats = {
            "STR": 50,
            "DEX": -1,
            "INT": 5,
            "WIS": 300
        }
        return stats


# Concrete builder
class WizardBuilder(CharacterBuilder):
    def get_category(self):
        return "Wizard"

    def get_items(self):
        return ["Magic wand", "Wizard's hat", "Estrogen"]

    def get_abilities(self):
        return ["Turn water into wine", "Cry", "Die for our sins"]

    def get_max_health(self):
        return 100

    def get_stats(self):
        stats = {
            "STR": 1,
            "DEX": -1,
            "INT": 1,
            "WIS": 1
        }
        return stats

    #     self.character = {}
    #
    #     self.character['health'] = 100       # Set default health to 100
    #     self.character['stats'] = {}         # Empty dict for stats, can be filled only during editing
    #     self.character['inventory'] = []     # Empty list for inventory, can be filled only during editing
    #     self.character['abilities'] = []     # Empty list for abilities, can be filled only during editing
    #
    # def create_char(self, name, character_class, history):
    #     self.character['name'] = name
    #     self.character['class'] = character_class
    #     self.character['history'] = history
    #
    # @validate_stat_input
    # @validate_stat_values
    # def set_stat(self, stat_name, value):
    #     self.character['stats'][stat_name] = value
    #
    # def add_ability(self, ability):
    #     self.character['abilities'].append(ability)
    #
    # def remove_ability(self, ability):
    #     self.character['abilities'].remove(ability)
    #
    # def add_item_to_inventory(self, item):
    #     self.character['inventory'].append(item)
    #
    # def remove_item_from_inventory(self, item):
    #     self.character['inventory'].remove(item)

