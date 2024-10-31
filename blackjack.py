# from deck_standard import deck

if __name__ == "__main__":

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
