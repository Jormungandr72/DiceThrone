from abc import ABC, abstractmethod
from random import Random

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

    def __init__(self):
        """
        Default constructor. Constructs a Character object with 25 hp, 2 cp, an 
        empty deck, and an empty hand.
        """
        super().__init__()
        self._hp = 25
        self._cp = 2
        self._deck = []
        self._hand = []
        self._discard = []

    # Getters

    def getHp(self):
        """
        Returns the hp stat of the character.
        Returns:
            int: the hp stat of the characters
        """
        return self._hp
    
    def getCp(self):
        """
        Returns the cp stat of the character.
        Returns:
            int: the cp stat of the character
        """
        return self._cp
    # Setters

    def setHp(self, newHp):
        """
        Updates the hp stat of the character.
        Args:
            newHp (int): the updated hp stat of the character
        """
        self._hp = newHp

    def setCp(self, newCp):
        """
        Updated the cp stat of the character.
        Args:
            newCp (int): the updated cp stat of the character
        """
        self._cp = newCp

    # Methods
    
    def draw(self, numToDraw):
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