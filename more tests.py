import random

user = input("What is your name?: ")
balance = 100


# functions
def spin_row():
    symbols = ['7️⃣', '🪙', '🔔', '💎']

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '7️⃣':
            return bet * 3
        elif row[0] == '🪙':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '💎':
            return bet * 10
    return 0


def main():
    balance = 100


card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in cards_list]


def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])


random.shuffle(deck)
pc = [deck.pop(), deck.pop()]
dc = [deck.pop(), deck.pop()]

# input to decide what next
# also the game Craps will be added someday but uh the doc draft didn't mention it so yeah
print("Casino Royale!")
print("")
print(f"Welcome {user}, What would you like to do?")
print("1) Play Blackjack")
print("2) Play the Slot Machine")
print("3) Read a guide")
print("4) Walk out (quit)")
menuchoice = int(input("I pick option: "))

bet = 0
# output
if menuchoice == 1:
    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            break


        while True:
            ps = sum(card_value(card) for card in pc)
            ds = sum(card_value(card) for card in dc)
            print("Cards Player Has:", pc)
            print("Score Of The Player:", ps)
            print("\n")
            choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower()
            if choice == "play":
                nc = deck.pop()
                pc.append(nc)
            elif choice == "stop":
                break
            else:
                print("Invalid choice. Please try again.")
                continue

            if ps > 21:
                balance = balance - bet
                print("Cards Dealer Has:", dc)
                print("Score Of The Dealer:", ds)
                print("Cards You Have:", pc)
                print("Your Score:", ps)
                print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
                print(f"Current balance: ${balance}")

                break

        while ds < 17:
            nc = deck.pop()
            dc.append(nc)
            ds += card_value(nc)

        print("Cards Dealer Has:", dc)
        print("Score Of The Dealer:", ds)
        print("\n")

        if ds > 21 and ps > 21:
            print("Cards Dealer Has:", dc)
            print("Score Of The Dealer:", ds)
            print("Cards You Have:", pc)
            print("Your Score:", ps)
            print("It's a tie.")
            print(f"Current balance: ${balance}")
        elif ds > 21:
            balance = balance + (bet * 2)
            print("Cards Dealer Has:", dc)
            print("Score Of The Dealer:", ds)
            print("Cards You Have:", pc)
            print("Your Score:", ps)
            print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)")
            print(f"Current balance: ${balance}")
        elif ps > 21:
            balance = balance - bet
            print("Cards Dealer Has:", dc)
            print("Score Of The Dealer:", ds)
            print("Cards You Have:", pc)
            print("Your Score:", ps)
            print("Dealer wins (Player Loss Because Dealer Score is exceeding 21)")
            print(f"Current balance: ${balance}")
        elif ps > ds:
            balance = balance + (bet * 2)
            print("Cards Dealer Has:", dc)
            print("Score Of The Dealer:", ds)
            print("Cards You Have:", pc)
            print("Your Score:", ps)
            print("Player wins (Player Has Higher Score than Dealer)")
            print(f"Current balance: ${balance}")
        elif ds > ps:
            balance = balance - bet
            print("Cards Dealer Has:", dc)
            print("Score Of The Dealer:", ds)
            print("Cards You Have:", pc)
            print("Your Score:", ps)
            print("Dealer wins (Dealer Has Higher Score than Player)")
            print(f"Current balance: ${balance}")
        else:
            print("Cards Dealer Has:", dc)
            print("Score Of The Dealer:", ds)
            print("Cards You Have:", pc)
            print("Your Score:", ps)
            print("It's a tie.")
            print(f"Current balance: ${balance}")

if menuchoice == 3:
    print("Blackjack ")
    print("You will make a bet and the game will start shortly after")
    print("You get cards and your score is the sum of the cards' value")
    print("The winner is whoever has more score by the time both players stop")
    print("The loser is either who had the least score or who had their score exceed 21")
    print("If you want to stop playing, make your bet 0")
    print("Slots")
    print("You will make a bet and the machine will roll")
    print("You win if the same symbol is rolled 3 in a row and lose otherwise")
    print("Your payout is decided by your winning symbol or if you lost")

if menuchoice == 2:
    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: 7️⃣ 🪙 🔔 💎 ")
    print("*************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()