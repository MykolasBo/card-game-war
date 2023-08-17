import random

class DeckOfCards:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.deck = [{'suit': suit, 'value': value} for suit in self.suits for value in self.values]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def split_deck(self):
        middle = int(len(self.deck)/2)
        first_half = self.deck[:middle]
        second_half = self.deck[middle:]
        return first_half, second_half

class Player:
    def __init__(self, hand, name="pc"):
        self.name = name
        self.hand = hand 

def main():
    deck = DeckOfCards()
    deck.shuffle_deck()
    first_half, second_half = deck.split_deck()

    name = input("Please provide your name: ")
    player_1 = Player(first_half, name)
    player_2 = Player(second_half)

#    starting_player = random.choice([player_1, player_2])

# [Priekis, A, B, C, D, Galas]

    while True:
        if not player_1.hand or not player_2.hand:
            break
        while True:
            card_1 = player_1.hand.pop()
            card_2 = player_2.hand.pop()
            war_cards = []
            if card_1["value"] > card_2["value"]:
                player_1.hand.insert(0, card_1)
                player_1.hand.insert(0, card_2)
                break
            elif card_1["value"] < card_2["value"]:
                player_2.hand.insert(0, card_1)
                player_2.hand.insert(0, card_2)
                break
            else:
                war_cards.append(card_1)
                war_cards.append(card_2)
                war_cards.append(player_1.hand.pop())
                war_cards.append(player_2.hand.pop())    

if __name__ == '__main__':
    main()

        