from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class StandardDeck:
    ranks: list = [i for i in range(2, 11)] + 'J Q K A'.split()
    suits: list = 'ouros copas espadas paus'.split()

    def __init__(self) -> None:
        self._cards: list = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

if __name__ == "__main__":
    my_deck = StandardDeck()
    print(my_deck[:13])

    specific_card = Card(7, 'bolinha')
    specific_card_2 = Card(7, 'paus')

    print(specific_card in my_deck)
    print(specific_card_2 in my_deck)

    print(len(my_deck))

# Exemplo com base no livro Fluent Python
