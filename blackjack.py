import random
from deck_standard import deck
# Due to certain changes in drawing a card during the game.
# Not importing draw_card function.


def draw_game_card(deck):
    card, (value, has_been_drawn) = random.choice(list(deck.items()))

    if not has_been_drawn:
        deck[card] = (value, True)
        return card
    else:
        return draw_game_card(deck)


def find_card_value(total, next_value, aces_count):
    if isinstance(next_value, list):  # If it's an Ace.

        if total + 11 <= 21:
            total += 11  # Ace is 11.
            aces_count += 1
        else:
            total += 1  # Ace is 1.
    else:
        total += next_value

    # For each Ace that equals 11...
    # Decrease total by 10 & Ace Count by 1.
    while total > 21 and aces_count > 0:
        total -= 10
        aces_count -= 1

    return total, aces_count


def calculate_hand_total(hand):
    total = 0
    aces_count = 0

    for card in hand:
        value, _ = deck[card]
        total, aces_count = find_card_value(total, value, aces_count)

    return total


if __name__ == "__main__":

    round_count = 0

    while True:
        print("Do you want to play Blackjack? (y/n)")

        res = input("Choice: ")
        res = res.lower()

        if res == "y":
            break
        elif res == "n":
            print("Exiting...")
            exit()
        else:
            print("Invalid response. Please try again.")

    while True:
        round_count += 1

        p_card1 = draw_game_card(deck)  # Player's 1st Card
        p_card2 = draw_game_card(deck)  # Player's 2nd Card
        player_hand = [p_card1, p_card2]  # Player's Hand
        player_total = calculate_hand_total(player_hand)

        d_card1 = draw_game_card(deck)  # Dealer's 1st Card
        d_card2 = draw_game_card(deck)  # Dealer's 2nd Card
        dealer_hand = [d_card1, d_card2]  # Dealer's Hand
        dealer_total = calculate_hand_total(dealer_hand)

        print("")
        print(f"Round: {round_count}")
        print("")

        print(f"You have been dealt The {p_card1} and The {p_card2}.")

        if player_total == 21:
            print("Your hand is at 21. Blackjack!")
            exit()
        else:
            print(f"Your hand is at {player_total}.\n"
                  f"Dealer is showing The {d_card1}.")

            print("Press Enter to continue...")
            input()

            while True:  # Nested while loop for player actions.
                print("What would you like to do?\n"
                      "1. Hit\n"
                      "2. Stand\n"
                      "3. View Dealer's Card")

                action = input("Choice: ")

                if action == "1":
                    drawn_card = draw_game_card(deck)
                    player_hand.append(drawn_card)
                    player_total = calculate_hand_total(player_hand)

                    print(f"You hit for The {drawn_card}.")

                    if player_total > 21:
                        print(f"Your hand is at {player_total}. Bust!")
                        break
                    elif player_total == 21:
                        print("Your hand is at 21. Blackjack!")
                        break
                    else:
                        print(f"Your hand is at {player_total}.")
                        continue

                elif action == "2":
                    print(f"You chose to stand at {player_total}.")
                    continue

                elif action == "3":
                    print(f"Dealer is showing The {d_card1}.")
                    continue

                else:
                    print("Invalid action. Plase try again.")

        break
