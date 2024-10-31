import random

deck = {
    # Clubs
    "2 of Clubs": (2, False),
    "3 of Clubs": (3, False),
    "4 of Clubs": (4, False),
    "5 of Clubs": (5, False),
    "6 of Clubs": (6, False),
    "7 of Clubs": (7, False),
    "8 of Clubs": (8, False),
    "9 of Clubs": (9, False),
    "10 of Clubs": (10, False),
    "Jack of Clubs": (10, False),
    "Queen of Clubs": (10, False),
    "King of Clubs": (10, False),
    "Ace of Clubs": ([1, 11], False),

    # Diamonds
    "2 of Diamonds": (2, False),
    "3 of Diamonds": (3, False),
    "4 of Diamonds": (4, False),
    "5 of Diamonds": (5, False),
    "6 of Diamonds": (6, False),
    "7 of Diamonds": (7, False),
    "8 of Diamonds": (8, False),
    "9 of Diamonds": (9, False),
    "10 of Diamonds": (10, False),
    "Jack of Diamonds": (10, False),
    "Queen of Diamonds": (10, False),
    "King of Diamonds": (10, False),
    "Ace of Diamonds": ([1, 11], False),

    # Spades
    "2 of Spades": (2, False),
    "3 of Spades": (3, False),
    "4 of Spades": (4, False),
    "5 of Spades": (5, False),
    "6 of Spades": (6, False),
    "7 of Spades": (7, False),
    "8 of Spades": (8, False),
    "9 of Spades": (9, False),
    "10 of Spades": (10, False),
    "Jack of Spades": (10, False),
    "Queen of Spades": (10, False),
    "King of Spades": (10, False),
    "Ace of Spades": ([1, 11], False),

    # Hearts
    "2 of Hearts": (2, False),
    "3 of Hearts": (3, False),
    "4 of Hearts": (4, False),
    "5 of Hearts": (5, False),
    "6 of Hearts": (6, False),
    "7 of Hearts": (7, False),
    "8 of Hearts": (8, False),
    "9 of Hearts": (9, False),
    "10 of Hearts": (10, False),
    "Jack of Hearts": (10, False),
    "Queen of Hearts": (10, False),
    "King of Hearts": (10, False),
    "Ace of Hearts": ([1, 11], False),
}


def draw_card(deck):
    card, (value, has_been_drawn) = random.choice(list(deck.items()))
    # (value = numeric value & has_been_drawn = boolean status)
    return card, (value, has_been_drawn)


if __name__ == "__main__":
    options = {
        "1": "Draw A Card",
        "2": "Shuffle Deck",
        "3": "Exit"
    }

    while True:
        print("Select an option:\n"
              "1: Draw A Card\n"
              "2: Shuffle Deck\n"
              "3: Exit")

        choice = input("Choice: ")
        if choice in options:

            if choice == "1":
                card, (value, has_been_drawn) = draw_card(deck)
                print(f"You drew the {card} with a value of {value}.")
                continue
            elif choice == "2":
                print("Shuffling the deck...\n"
                      "(functionality not implemented yet)")
                continue
            elif choice == "3":
                print("Exiting...")
                break
        else:
            print("Invalid choice. Please try again.")
