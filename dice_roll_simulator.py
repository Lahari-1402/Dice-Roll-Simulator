import random
def roll_dice():
    return random.randint(1, 6)

while True:
    user_input = input("Do you want to roll the dice? (yes/no): ").lower()
    if user_input == 'yes':
        print(f"You rolled a {roll_dice()}!")
    elif user_input == 'no':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
