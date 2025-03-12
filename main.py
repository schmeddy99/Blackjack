from art import logo
import random
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_total(hand):
    """Calculates the total of a given hand, adjusting Aces if necessary."""
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1  # Convert Ace (11) to 1
        total = sum(hand)
    return total

def display_hand(player, hand, total, hide_second_card=False):
    """Displays the player's or computer's hand."""
    if hide_second_card:
        print(f"{player}'s first card: {hand[0]}, second card is hidden.")
    else:
        print(f"{player}'s cards: {hand}, current score: {total}")

def blackjack():
    """Main function to run a game of Blackjack."""
    user_cards = random.choices(cards, k=2)
    computer_cards = [random.choice(cards), random.choice(cards)]

    user_total = calculate_total(user_cards)
    computer_total = calculate_total(computer_cards)

    display_hand("Your", user_cards, user_total)
    display_hand("Computer", computer_cards, computer_total, hide_second_card=True)

    # User's turn
    while user_total < 21:
        hit = input("Type 'y' to hit or 'n' to stand: ").lower()
        if hit == 'y':
            user_cards.append(random.choice(cards))
            user_total = calculate_total(user_cards)
            display_hand("Your", user_cards, user_total)

            if user_total > 21:
                print("You went over. You lose.")
                return
        else:
            break  # User stands
    
    # Computer's turn (DO NOT print full hand yet)
    time.sleep(1)  # Pause before revealing the computer's turn
    print("\nThe dealer (computer) starts playing...")

    # Computer's turn
    while computer_total < 17:
        time.sleep(1)
        computer_cards.append(random.choice(cards))
        computer_total = calculate_total(computer_cards)
        print(f"Computer hit. Computer's cards: {computer_cards}, score: {computer_total}")

    # NOW Reveal Final Computer Hand
    print(f"\nComputer's final hand: {computer_cards}, final score: {computer_total}")

    # Final comparison
    time.sleep(1) # Pause for suspense
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
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if continue_game == 'y':
        print(logo)
        blackjack()
    else:
        isActive = False
