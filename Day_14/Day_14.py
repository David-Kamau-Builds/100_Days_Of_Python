import random
import game_data
import art

print("Welcome to Higher or Lower. A guessing game.")
print(art.logo)

def get_random_item(exclude=None):
    """Return a random item from game_data, optionally excluding one."""
    item = random.choice(game_data.data)
    while exclude and item == exclude:
        item = random.choice(game_data.data)
    return item

def format_data(item):
    """Return formatted text for display."""
    return f"{item['name']}. {item['description']} from {item['country']}."

def game_logic():
    score = 0

    item_a = get_random_item()

    while True:
        item_b = get_random_item(exclude=item_a)  # ensures A != B

        print(f"\nCompare A: {format_data(item_a)}")
        print(art.vs)
        print(f"Against B: {format_data(item_b)}")

        guess = input("Pick A or B: ").lower()

        a_follow = item_a["follower_count"]
        b_follow = item_b["follower_count"]

        correct_answer = "a" if a_follow > b_follow else "b"

        if guess == correct_answer:
            score += 1
            print(f"\nCorrect. Your current score: {score}\n")

            item_a = item_a if correct_answer == "a" else item_b

        elif guess in ("a", "b"):
            print(f"\nYou lose. Final score: {score}")
            break
        else:
            print("Invalid input. Please type A or B.")

game_logic()