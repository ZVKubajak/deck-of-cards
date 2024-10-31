import random

deck = {
    # Clubs
    "2 of Clubs": 2,
    "3 of Clubs": 3,
    "4 of Clubs": 4,
    "5 of Clubs": 5,
    "6 of Clubs": 6,
    "7 of Clubs": 7,
    "8 of Clubs": 8,
    "9 of Clubs": 9,
    "10 of Clubs": 10,
    "Jack of Clubs": 10,
    "Queen of Clubs": 10,
    "King of Clubs": 10,
    "Ace of Clubs": [1, 11],

    # Diamonds
    "2 of Diamonds": 2,
    "3 of Diamonds": 3,
    "4 of Diamonds": 4,
    "5 of Diamonds": 5,
    "6 of Diamonds": 6,
    "7 of Diamonds": 7,
    "8 of Diamonds": 8,
    "9 of Diamonds": 9,
    "10 of Diamonds": 10,
    "Jack of Diamonds": 10,
    "Queen of Diamonds": 10,
    "King of Diamonds": 10,
    "Ace of Diamonds": [1, 11],

    # Spades
    "2 of Spades": 2,
    "3 of Spades": 3,
    "4 of Spades": 4,
    "5 of Spades": 5,
    "6 of Spades": 6,
    "7 of Spades": 7,
    "8 of Spades": 8,
    "9 of Spades": 9,
    "10 of Spades": 10,
    "Jack of Spades": 10,
    "Queen of Spades": 10,
    "King of Spades": 10,
    "Ace of Spades": [1, 11],

    # Hearts
    "2 of Hearts": 2,
    "3 of Hearts": 3,
    "4 of Hearts": 4,
    "5 of Hearts": 5,
    "6 of Hearts": 6,
    "7 of Hearts": 7,
    "8 of Hearts": 8,
    "9 of Hearts": 9,
    "10 of Hearts": 10,
    "Jack of Hearts": 10,
    "Queen of Hearts": 10,
    "King of Hearts": 10,
    "Ace of Hearts": [1, 11]
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
