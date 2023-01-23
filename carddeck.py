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

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"



class CardDeck:  # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}:{self.dealer}/{len(self)}"

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}('{self.dealer}')"

    def __init__(self, dealer):
        """
        Class constructor. Accepts dealer name as a string.
        """
        self._dealer = dealer  # store arg as private variable
        self._make_deck()

    def __len__(self):
        return len(self._cards)

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def dealer(self):  # getter property
        return self._dealer

    @property
    def udealer(self):
        return self._dealer.upper()

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def __add__(self, other_deck):
        new_deck = type(self)(self.dealer)
        new_deck._cards = self.cards + other_deck.cards
        return new_deck

