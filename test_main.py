from unittest import TestCase

from character import WarriorBuilder, Character, WizardBuilder
from manager import Director
class Test(TestCase):
    def test_wizard_default_fields(self):
        wizard_builder = WizardBuilder()
        director = Director()
        director.set_builder(wizard_builder)
        character = director.build_character()

        self.assertEqual(character.category, "Wizard")
        self.assertEqual(character.items, ["Magic wand", "Wizard's hat", "Estrogen"])
        self.assertEqual(character.abilities, ["Turn water into wine", "Cry", "Die for our sins"])