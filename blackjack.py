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


if __name__ == "__main__":

    round_count = 0
    card1 = draw_game_card(deck)
    card2 = draw_game_card(deck)

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

        print("")
        print(f"Round: {round_count}")
        print("")
        print(f"Card 1: {card1}")
        print(f"Card 2: {card2}")
        break
