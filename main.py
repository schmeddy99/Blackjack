import time
import random
from art import logo

# Define a dictionary to map face cards
card_values = {
    "A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10
}

def draw_card():
    """Randomly selects a card and returns its name and value."""
    card = random.choice(list(card_values.keys()))
    return card, card_values[card]

def calculate_total(hand_values):
    """Calculates the total value of a given hand, adjusting Aces if necessary."""
    total = sum(hand_values)
    while total > 21 and 11 in hand_values:
        hand_values[hand_values.index(11)] = 1  # Convert Ace (11) to 1
        total = sum(hand_values)
    return total

def display_hand(player, hand, total, hide_second_card=False):
    """Displays the player's or computer's hand."""
    if hide_second_card:
        print(f"{player}'s first card: {hand[0]}, second card is hidden.")
    else:
        print(f"{player}'s cards: {hand}, current score: {total}")

def player_turn(user_hand, user_values):
    """Handles the player's turn, allowing them to hit or stand."""
    while calculate_total(user_values) < 21:
        hit = input("Type 'y' to hit or 'n' to stand: ").lower()
        if hit == 'y':
            card, value = draw_card()
            user_hand.append(card)
            user_values.append(value)
            total = calculate_total(user_values)
            display_hand("Your", user_hand, total)

            if total > 21:
                print("You went over. You lose.")
                return total
        else:
            break
    return calculate_total(user_values)

def computer_turn(computer_hand, computer_values):
    """Handles the computer's turn, drawing cards until reaching 17 or higher."""
    print("\nThe dealer (computer) starts playing...")
    time.sleep(1)
    while calculate_total(computer_values) < 17:
        time.sleep(1)
        card, value = draw_card()
        computer_hand.append(card)
        computer_values.append(value)
        total = calculate_total(computer_values)
        print(f"Computer drew: {card}. Computer's cards: {computer_hand}, score: {total}")
    return calculate_total(computer_values)

def blackjack():
    """Main function to run a game of Blackjack."""
    user_hand = []
    user_values = []
    computer_hand = []
    computer_values = []

    # Deal initial two cards to player and dealer
    for _ in range(2):
        card, value = draw_card()
        user_hand.append(card)
        user_values.append(value)

    card, value = draw_card()
    computer_hand.append(card)
    computer_values.append(value)

    display_hand("Your", user_hand, calculate_total(user_values))
    display_hand("Computer", computer_hand, calculate_total(computer_values), hide_second_card=True)

    # User's turn
    user_total = player_turn(user_hand, user_values)
    if user_total > 21:
        return  # Ends game if player busts

    # Computer's turn
    computer_total = computer_turn(computer_hand, computer_values)
    print(f"\nComputer's final hand: {computer_hand}, final score: {computer_total}")

    # Final comparison
    time.sleep(1)
    if user_total > 21:
        print("You went over. You lose.")
    elif computer_total > 21:
        print("Computer went over. You win!")
    elif user_total > computer_total:
        print("You win!")
    elif user_total < computer_total:
        print("Computer wins!")
    else:
        print("It's a draw.")

# Game loop
isActive = True
while isActive:
    continue_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if continue_game == 'y':
        print(logo)
        blackjack()
    else:
        isActive = False
