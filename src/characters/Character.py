from abc import ABC, abstractmethod
from random import Random
from main.Phase import Phase as Phase
import json

class Character(ABC):
    """
    -------------------------------------------------------------------------------
    Program:    Character.py
    Author:     Patrick J. McGranahan
    Date:       04.25.2025
    Language:   python
    Purpose:    To serve as a base class for the characters in Dice Throne.
                contains methods to override.
    -------------------------------------------------------------------------------
    Change Log:
    Who  When           What
    PJM  04.29.2025     Updated phase trigger methods with a pass statement and
                        a comment that describes what to do. 
    PJM  04.29.2025     Added methods to trigger on different phases.
    PJM  04.29.2025     Added type annotations.
    PJM  04.25.2025     Updated the draw method with parameter numToDraw.
    PJM  04.25.2025     Added a getter and setter for _cp.
    PJM  04.25.2025     Added data field _discard, method draw(), and imported 
                        the random module.
    PJM  04.25.2025     Added a getter and setter for _hp.
    PJM  04.25.2025     Changed all data fields to private.
    PJM  04.25.2025     Created default constructor.
    PJM  04.25.2025     Created class Character, created comment block, added
                        abc import.
    -------------------------------------------------------------------------------
    """
    # Constructor

    def __init__(self) -> None:
        """
        Default constructor. Constructs a Character object with 25 hp, 2 cp, an 
        empty deck, and an empty hand.
        """
        super().__init__()
        self._hp: int = 25
        self._cp: int = 2
        self._deck: list = []
        self._hand: list = []
        self._discard: list = []

    # Getters

    def getHp(self) -> int:
        """
        Returns the hp stat of the character.
        
        Returns:
            int: the hp stat of the characters
        """
        return self._hp
    
    def getCp(self) -> int:
        """
        Returns the cp stat of the character.

        Returns:
            int: the cp stat of the character
        """
        return self._cp
    # Setters

    def setHp(self, newHp: int) -> None:
        """
        Updates the hp stat of the character.

        Args:
            newHp (int): the updated hp stat of the character
        """
        self._hp = newHp

    def setCp(self, newCp: int) -> None:
        """
        Updated the cp stat of the character.

        Args:
            newCp (int): the updated cp stat of the character
        """
        self._cp = newCp

    # Methods
    
    def draw(self, numToDraw: int) -> None:
        """
        Draws a card from the character's deck into their hand.

        Args:
            numToDraw (int): the number of cards to draw.
        """
        for i in numToDraw:
            if (self._deck.count > 0):
                self._hand.append(self._deck.pop())
            else:
              for i in self._discard.count():
                  self._deck.append(self._discard.pop())
              Random.shuffle(self._deck)
              self._hand.append(self._deck.pop)

    def shuffle(self) -> None:
        """
        Shuffles the character's deck.
        """
        Random.shuffle(self._deck)

    def loadDeck(self, deck_json: json) -> None:
        """
        Populates a character's deck with cards.

        Args:
            deck_json (json): the character-specific deck to load
        """
        pass # TODO implement based on character-specifc json

    def loadGenericDeck(self):
        """
        Adds all cards shared across characters to the character's deck.
        """
        pass # TODO implement based on generic_deck.json

    def phaseTrigger(self, phase: Phase) -> bool:
        """
        Checks for abilities that trigger in the phase specified by the function
        parameter.

        Args:
            phase (Phase): a Phase enum set to the current phase.

        Returns:
            bool: {True} if the a skill was triggered; {False} otherwise
        """
        if phase.UPKEEP:
            return self.upkeepTrigger()
        elif phase.INCOME:
            return self.incomeTrigger()
        elif phase.FIRST_MAIN:
            return self.firstMainTrigger()
        elif phase.OFFENSIVE_ROLL:
            return self.offensiveRollTrigger()
        elif phase.TARGETING:
            return self.targetingTrigger()
        elif phase.DEFENSIVE_ROLL:
            return self.defensiveRollTrigger()
        elif phase.SECOND_MAIN:
            return self.secondMainTrigger()
        elif phase.DISCARD:
            return self.discardTrigger()
        
    @abstractmethod
    def upkeepTrigger() -> bool:
        """
        Triggers character specific abilities that occur in the upkeep phase.
        
        Returns:
            bool: {True} if a skill was triggered; {False} otherwise
        """
        pass # TODO implement based on character-specifc json

    @abstractmethod
    def incomeTrigger() -> bool:
        """
        Triggers character specific abilities that occur in the income phase.

        Returns:
            bool: {True} if a skill was triggered; {False} otherwise
        """
        pass # TODO implement based on character-specifc json

    @abstractmethod
    def firstMainTrigger() -> bool:
        """
        Triggers character specific abilities that occur in the first main phase.
        
        Returns:
            bool: {True} if a skill was triggered; {False} otherwise
        """
        pass # TODO implement based on character-specifc json

    @abstractmethod
    def offensiveRollTrigger() -> bool:
        """
        Triggers character specific abilities that occur in the offensive roll phase.

        Returns:
            bool: {True} if a skill was triggered; {False} otherwise
        """
        pass # TODO implement based on character-specifc json
        
    @abstractmethod
    def targetingTrigger() -> bool:
        """
        Triggers character specific abilities that occur in the targeting phase.
        
        Returns:
            bool: {True} if a skill was triggered; {False} otherwise
        """
        pass # TODO implement based on character-specifc json

    @abstractmethod
    def defensiveRollTrigger() -> bool:
        """
        Triggers character specific abilities that occur in the defensive roll phase.

        Returns:
            bool: {True} if a skill was triggered; {False} otherwise
        """
        pass # TODO implement based on character-specifc json

    @abstractmethod
    def secondMainTrigger() -> bool:
        """
        Triggers character specific abilities that occur in the second main phase.

        Returns:
            bool: {True} if a skill was triggered; {False} otherwise
        """
        pass # TODO implement based on character-specifc json

    @abstractmethod
    def discardTrigger() -> bool:
        """
        Triggers character specific abilities that occur in the discard phase.

        Returns:
            bool: {True} if a skill was triggered; {False} otherwise
        """
        pass # TODO implement based on character-specifc json