import unittest
from src.characters.Character import Character

class TestCharacter(unittest.TestCase):
    """
    -------------------------------------------------------------------------------
    Program:    TestCharacter.py
    Author:     Patrick J. McGranahan
    Date:       09.10.2025
    Language:   python
    Purpose:    The purpose of this code is to test the character class's 
                functionality.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  09.10.2025     Added code to instantiate a Character object to test.
    PJM  09.10.2025     Created TestCharacter.py.
    -------------------------------------------------------------------------------
    """
    _sample_class: Character = Character()

    def test_getters(self):
        """
        Tests whether the getters in the Character class are working as expected.
        """
        self.assertEqual(Character._hp, Character.getHp())
        self.assertEqual(Character._cp, Character.getCp())

if __name__ == "__main__":
    unittest.main()