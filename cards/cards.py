import random as rand

def create_deck():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    suits = ["s", "h", "d", "c"]

    deck = []
    # Generating every possible card
    # outer loop goes through each value 2 - Ace
    # For every value, inner loop goes through each suit
    # inner loop adds the concatenation of value and suit to the deck
    # i.e val = "J" suit = "c", deck.append ("J" + "c") == deck.append("Jc")
    for val in values:
        for suit in suits:
            deck.append(val + suit)

    return deck

def shuffle(cards):
    new_cards = cards.copy()

    for i in range(0, 100):
        rand1 = rand.randint(0, 51)
        rand2 = rand.randint(0, 51)
        # Swap two random elements in new_cards list
        temp = new_cards[rand1]
        new_cards[rand1] = new_cards[rand2]
        new_cards[rand2] = temp


    return new_cards

def deal(number_of_hands, number_of_cards, cards):
    hands = []
    for i in range(0, number_of_hands):
        hand = []

        for j in range(0, number_of_cards):
            hand.append(cards.pop(0))

        hands.append(hand)

    return hands

def print_hands(hands):
    names = ["Emile", "Kelley", "Henry", "Leon"]

    for i in range(0, len(hands)):
        line = names[i] + "'s hand: "

        for j in range(0, len(hands[i])):
            line += hands[i][j] + " "

        print(line)

def main():
    deck = create_deck()

    new_deck = shuffle(deck)

    print_hands(deal(4,2,new_deck))

if __name__ == "__main__":
    main()
