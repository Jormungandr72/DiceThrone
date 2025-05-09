from enum import Enum

class Phase(Enum):
    """
    -------------------------------------------------------------------------------
    Program:    Phase.py
    Author:     Patrick J. McGranahan
    Date:       04.29.2025
    Language:   python
    Purpose:    The purpose of this enumerated class is to represent phases in the
                dice throne program.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  04.29.2025     Created Phase.py, added all phases.
    -------------------------------------------------------------------------------
    """
    UPKEEP = 1
    INCOME = 2
    FIRST_MAIN = 3
    OFFENSIVE_ROLL = 4
    TARGETING = 5
    DEFENSIVE_ROLL = 6
    SECOND_MAIN = 7
    DISCARD = 8