from characters import Character
from main.Phase import Phase as Phase 

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
    def __init__(self, characterOne: Character, characterTwo: Character) -> None:
        """
        Constructs a GameLoop object with two characters.
        Args:
            characterOne (Character): the first character to run the game with
            characterTwo (Character): the second character to run the game with
        """
        self._firstChar: Character = characterOne
        self._secondChar: Character = characterTwo
        self._turnChar: Character = self._firstChar
        self._phase = Phase

    # Methods
    def run(self) -> None:
        """
        Runs the gameloop until a character has been reduced to 0 hp.
        """
        while (self.firstChar.getHp() > 0 and self.secondChar.getHp() > 0):
            return None # Not currently implemented

            # Upkeep Phase
            self._phase.UPKEEP
            self._firstChar.phaseTrigger(self._phase)
            self._secondChar.phaseTrigger(self._phase)

            # Income Phase
            self._phase.INCOME
            # TODO run a method to check for abilites that trigger during upkeep
            self._turnChar.setCp(self._turnChar.getCp() + 1)
            self._turnChar.draw(1)