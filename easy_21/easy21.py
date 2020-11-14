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

    # Swap two random elements in new_cards list 100 times to shuffle
    for i in range(0, 100):
        rand1 = rand.randint(0, 51)
        rand2 = rand.randint(0, 51)
        temp = new_cards[rand1]
        new_cards[rand1] = new_cards[rand2]
        new_cards[rand2] = temp


    return new_cards

def deal(number_of_hands, number_of_cards, cards):
    hands = [] # This list will hold list of strings (2D array)
    for i in range(0, number_of_hands):
        hand = [] # This list will hold card values

        for j in range(0, number_of_cards):
            hand.append(cards.pop(0)) # Get cards from deck to hand

        hands.append(hand) # Add completed hand to list of hands

    return hands

def print_hands(hands):
    names = ["Emile", "Kelley", "Henry", "Leon"]

    for i in range(0, len(hands)):
        line = names[i] + "'s hand: "

        for j in range(0, len(hands[i])):
            line += hands[i][j] + " "

        print(line)

def init_easy_21():
    num_hands = 0

    # Get the number of hands to deal from user (with input validation)
    while True:
        print("Welcome to Easy 21!\nHow many hands to deal? (1-4)")
        num_hands = input("> ")
        
        if int(num_hands) >= 1 and int(num_hands) <= 4:
            num_hands = int(num_hands)
            break

    # Deck and hand initialization
    deck = create_deck()
    deck = shuffle(deck)
    hands = deal(num_hands, 2, deck)

    # Print initial hands
    print("Dealt " + str(num_hands) + " hands, 2 cards each")
    print_hands(hands)

    return deck, hands

def start_game(deck, hands):
    while True:
        # Deck being empty is an end game condition
        if len(deck) == 0:
            end_game(hands)
            break # Used to break out of game loop
        
        # This loop reads in the users selection for playing the game
        # it makes it uppercase so that upper and lowercase inputs get accepted
        selection = ""
        while True:
            print("Select\n\tD: draw\n\tS: stand\n\tW: show hands\n\tC: show deck\n\tQ: quit")
            selection = input("> ")
            selection = selection.upper()

            options = ['D', 'S', 'W', 'C', 'Q']
            if selection in options:
                break
            else:
                print("Invalid option, please try again")

        # Run a specific function based on the input 
        if selection == 'D':
            hands = draw_to_hand(deck, hands)
        if selection == 'S':
            end_game(hands)
            break # Used to break out of game loop
        if selection == 'W':
            print_hands(hands)
        if selection == 'C':
            print(deck)
        if selection == 'Q':
            exit()

def draw_to_hand(deck, hands):
    hand_num = 0
    # Determine which hand user would like to draw card to (with input validation)
    while True:
        print("Which hand would you like to draw to? (1-" + str(len(hands)) + ")")
        hand_num = input(">")
        
        if int(hand_num) >= 1 and int(hand_num) <= len(hands):
            hand_num = int(hand_num)
            break
        else:
            print("Invalid input, please try again")

    # Add card to chosen hand (hand_num - 1 because lists are 0-indexed)
    hands[hand_num - 1].append(deck.pop(0))

    # Print updated hands
    print_hands(hands)

    return hands

def end_game(hands):
    max_sum = 0
    max_hand = 0
    # For every hand, calculate the sum of cards based on the value (2-9, T-K, and A)
    for i in range(len(hands)):
        sum = 0
        for card in hands[i]:
            if ord(card[0]) >= 50 and ord(card[0]) <= 57: # If ascii value matches chars in range: 2-9
                sum += ord(card[0]) - 48
            elif ord(card[0]) == 74 or ord(card[0]) == 75 or ord(card[0]) == 81 or ord(card[0]) == 84: # if ascii value is any of the following: J,Q,K,T
               sum += 10
            elif ord(card[0]) == 65: # if ascii value matches: A
                if(sum + 11) > 21:
                    sum += 1
                else:
                    sum += 11
        # If the hands sum is more than the current max and is at or below 21, make it the new max
        if sum <= 21 and sum > max_sum:
            max_sum = sum
            max_hand = i + 1
    # Print calculated max hand with its sum
    print("Hand " + str(max_hand) + " won this round with " + str(max_sum) + " points!")


            
def main():
    deck, hands = init_easy_21()
    start_game(deck, hands)

if __name__ == "__main__":
    main()