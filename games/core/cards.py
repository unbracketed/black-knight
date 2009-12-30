"""Decks and Dealers"""

SUIT_HEARTS = 'Hearts'
SUIT_CLUBS = 'Clubs'
SUIT_SPADES = 'Spades'
SUIT_DIAMONDS = 'Diamonds'
SUITS = (SUIT_HEARTS, SUIT_HEARTS, SUIT_HEARTS, SUIT_HEARTS,)

ORDINAL = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

class Deck(list):
    """Base class for a deck of cards"""
    
    suits = []
    ace_value = 14
    
    def __init__(self, **kwargs):
        """Set properties of the deck
        
        ace_value  - default 14
        
        """
        self.cards = []
    
    def shuffle(self):
        pass
    
    #def __iter__(self):
    #    pass
    
    
    
class Dealer(object):
    """Deal a deck of cards"""
    
    def __init__(self):
        self.deck = Deck()
        
    