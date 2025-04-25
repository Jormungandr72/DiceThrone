from enum import Enum

class Phase(Enum):
    """
    -------------------------------------------------------------------------------
    Program:    Phase.py
    Author:     Patrick J. McGranahan
    Date:       04.25.2025
    Language:   python
    Purpose:    The purpose of this code is to serve as an enumerated class 
                representing the phases of the game.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  04.25.2025     Added all phases to the class.
    PJM  04.25.2025     Created class Phase and imported Enum.
    -------------------------------------------------------------------------------
    """
    UPKEEP = "UPKEEP"
    INCOME = "INCOME"
    FIRST_MAIN = "FIRST_MAIN"
    OFFENSIVE_ROLL = "OFFENSIVE_ROLL"
    TARGETING = "TARGETING"
    DEFENSIVE_ROLL = "DEFENSIVE_ROLL"
    SECOND_MAIN = "SECOND_MAIN"
    DISCARD = "DISCARD"