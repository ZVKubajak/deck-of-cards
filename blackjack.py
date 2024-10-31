import deck as d
print(f"{d}")

if __name__ == "__main__":
    menu = {
        "y": "Play",
        "n": "Exit"
    }

    while True:
        print("Do you want to play Blackjack? (y/n)")

        choice = input("Choice: ")
        choice = choice.lower()

        if choice in menu:

            if choice == "y":
                continue
            elif choice == "n":
                break
        else:
            print("Invalid choice. Please try again.")
