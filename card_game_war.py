import random


class DeckOfCards:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    def __init__(self):
        self.deck = [
            {"suit": suit, "rank": rank} for suit in self.suits for rank in self.ranks
        ]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def split_deck(self):
        first_half = self.deck[: int(len(self.deck) / 2)]
        second_half = self.deck[int(len(self.deck) / 2) :]
        return first_half, second_half


class Player:
    def __init__(self, hand, name="Computer"):
        self.hand = hand
        self.name = name


def main():
    deck = DeckOfCards()
    deck.shuffle_deck()
    first_half, second_half = deck.split_deck()

    name = input("Please provide your name: ")
    user = Player(first_half, name)
    computer = Player(second_half)

    while True:
        if not user.hand:
            print("Computer has won!")
            break
        elif not computer.hand:
            print(f"{user.name} has won!")
            break
        else:
            game_turn(user, computer)


def game_turn(user, computer, war_cards=None):
    if war_cards is None:
        war_cards = []
    card_1 = user.hand.pop()
    card_2 = computer.hand.pop()
    war_cards.append(card_1)
    war_cards.append(card_2)
    if card_1["rank"] > card_2["rank"]:
        user.hand = war_cards + user.hand
        # user.hand.insert(0, card_1)
        # user.hand.insert(0, card_2)
    elif card_1["rank"] < card_2["rank"]:
        computer.hand = war_cards + computer.hand
        # computer.hand.insert(0, card_1)
        # computer.hand.insert(0, card_2)
    else:
        try:
            war_cards.append(user.hand.pop())
            war_cards.append(computer.hand.pop())
        except IndexError:
            return
        try:
            game_turn(user, computer, war_cards)
        except IndexError:
            return


if __name__ == "__main__":
    main()

        