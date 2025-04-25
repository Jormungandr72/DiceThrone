from enum import Enum

class GameLoop:
    """
    -------------------------------------------------------------------------------
    Program:    GameLoop.py
    Author:     Patrick J. McGranahan
    Date:       04.25.2025
    Language:   python
    Purpose:    To provide methods for running the primary game loop.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  04.25.2025     Imported Enum for the _phase data field, and added 
                        _turnChar data field.
    PJM  04.25.2025     Added _phase field and made all data fields private.
    PJM  04.25.2025     Deleted default constructor and added one with two 
                        arguments, one for each character in the battle.
    PJM  04.25.2025     Created default constructor.
    PJM  04.25.2025     Created class GameLoop, created comment block.
    -------------------------------------------------------------------------------
    """
    # Constructor
    def __init__(self, characterOne, characterTwo):
        """
        Constructs a GameLoop object with two characters.
        Args:
            characterOne (Character): the first character to run the game with
            characterTwo (Character): the second character to run the game with
        """
        self._firstChar = characterOne
        self._secondChar = characterTwo
        self._turnChar = self._firstChar
        self._phase = Enum('Phase', [('UPKEEP', 1), ('INCOME', 2), ('FIRST_MAIN', 3), 
                                     ('OFFENSIVE_ROLL', 4), ('TARGETING', 5), 
                                     ('DEFENSIVE_ROLL', 6), ('SECOND_MAIN', 7),
                                     ('DISCARD', 8)])

    # Methods
    def run(self):
        """
        Runs the gameloop until a character has been reduced to 0 hp.
        """
        while (self.firstChar.getHp() > 0 and self.secondChar.getHp() > 0):
            self.firstChar.setHp(0) # Unimplemented loop

            # Upkeep Phase
            self._phase.UPKEEP

            # Income Phase
            self._phase.INCOME
            self._turnChar.setCp(self._turnChar.getCp() + 1)
            self._turnChar.draw(1)