import art
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

bidDictionary = {}
continueBidding = "y"

clear_screen()
print(art.logo)
print("Welcome to our Bidding Platform!")

while continueBidding == "y":
    clear_screen()
    print(art.logo)
    
    userName = input("What is your name? ")
    
    bidValid = False
    while not bidValid:
        try:
            bidPrice = int(input("What is your bid price? $"))
            if bidPrice > 0:
                bidValid = True
            else:
                print("Bid must be a positive number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number for your bid.")
            
    bidDictionary[userName] = bidPrice
    
    continueBidding = input("Would you like to continue bidding? y/n: ").lower()

else:
    clear_screen()
    print(art.logo)
    print("Thank you for playing!")

    if bidDictionary:
        highestBid = max(bidDictionary.values())
        winnerUserName = ""
        
        for key, value in bidDictionary.items():
            if value == highestBid:
                winnerUserName = key
                break

        print(f"Our winner is: {winnerUserName}. With a bid of: ${highestBid}")
    else:
        print("No bids were placed.")
        