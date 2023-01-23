
from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call method in ancestor
        for joker in range(2):
            card = Card('JOKER', 'JOKER')
            self._cards.append(card)


