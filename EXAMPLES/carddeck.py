"""
Provide a CardDeck object and some utility methods
"""
import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @rank.setter
    def rank(self, value):
        pass

    def __repr__(self):
        return f"Card('{self._rank}', '{self._suit}')"

    def __str__(self):
        return f"{self.rank}-{self.suit}"

class CardDeck:
    """
    A deck of 52 cards for playing standard card games
    """
    # def __new__(): pass
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    CLUB = '\u2663'
    DIAMOND = '\u2666'
    HEART = '\u2665'
    SPADE = '\u2660'
    SUITS = CLUB, DIAMOND, HEART, SPADE
    DEALER_NAMES = []

    def __init__(self, dealer_name):
        """
        CardDeck constructor

        :param dealer_name: Name of dealer as a string
        """
        self.dealer_name = dealer_name
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def draw(self):
        """
        Retrieve next available card from deck.

        Raises IndexError when deck is empty.

        :return: One cards as a (rank, suit) tuple.
        """
        try:
            return self._cards.pop(0) #
        except IndexError:
            print("Sorry, no more cards")

    def shuffle(self):
        """
        Randomize the deck of cards

        :return: None
        """
        random.shuffle(self._cards)

    @property
    def dealer_name(self):  # getter property
        """
        Set/Retrieve the dealer.

        If invalid type is assigned, raises TypeError

        :return: Dealer as a string
        """
        return self._dealer_name

    @dealer_name.setter
    def dealer_name(self, value):  # setter property
        if isinstance(value, str):
            self._dealer_name = value
        else:
            raise TypeError("Dealer must be a string")

    @property
    def cards(self):
        """
        Retrieve cards

        :return:  tuple of remaining cards
        """
        return tuple(self._cards) # make it read-only

    @classmethod
    def get_ranks(cls):
        """
        Return ranks as a list

        :return:
        """
        return cls.RANKS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer_name},{len(self)})"

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"""{my_name}("{self.dealer_name}")"""

    def __add__(self, other):
        my_type = type(self)
        tmp = my_type(self.dealer_name)
        tmp._cards = self._cards + other._cards
        return tmp

    def __eq__(self, other):
        return (
            self._dealer_name == other.dealer
            and
            self._cards == other._cards
        )

if __name__ == '__main__':
    d = CardDeck("Mary")
    d.shuffle()
    print(d.cards)
