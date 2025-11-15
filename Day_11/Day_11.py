import random
import art
import os

print(art.logo)
print("Welcome to the BlackJack game.")

def clear_screen():
    if os.getenv("TERM"):
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("\n" * 80)


cardDictionary = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": [1, 11]
}

def draw_user_card():
    card = random.choice(list(cardDictionary.keys()))
    if card == "Ace":
        choice = input("You drew an Ace! Enter '1' or '11': ")
        while choice not in ["1", "11"]:
            choice = input("Invalid choice. Enter '1' or '11': ")
        return int(choice)
    return cardDictionary[card]

def draw_computer_card(current_total):
    card = random.choice(list(cardDictionary.keys()))
    if card == "Ace":
        return 11 if current_total + 11 <= 21 else 1
    return cardDictionary[card]

def calculate_total(card_list):
    return sum(card_list)

def compare_scores(user_total, computer_total):
    if user_total == computer_total:
        return "It's a draw."
    elif user_total > 21:
        return "You lost. You busted."
    elif computer_total > 21:
        return "Computer busted. You win!"
    elif user_total > computer_total:
        return "You win!"
    else:
        return "Computer wins."

def play():
    print(art.logo)
    user_cards = []
    computer_cards = []

    user_cards.append(draw_user_card())
    user_cards.append(draw_user_card())

    computer_cards.append(draw_computer_card(0))
    computer_cards.append(draw_computer_card(sum(computer_cards)))

    while True:
        user_total = calculate_total(user_cards)
        print(f"Your cards: {user_cards}, total: {user_total}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_total >= 21:
            break

        choice = input("Type 'y' to draw another card, 'n' to stop: ").lower()
        if choice == "y":
            user_cards.append(draw_user_card())
        else:
            break

    while calculate_total(computer_cards) < 17:
        computer_cards.append(draw_computer_card(calculate_total(computer_cards)))

    user_total = calculate_total(user_cards)
    computer_total = calculate_total(computer_cards)

    print(f"\nYour final hand: {user_cards}, final total: {user_total}")
    print(f"Computer final hand: {computer_cards}, final total: {computer_total}")
    print(compare_scores(user_total, computer_total))


while input("Do you want to play Blackjack? (y/n): ").lower() == "y":
    clear_screen()
    play()
