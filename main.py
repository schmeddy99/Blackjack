from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

isActive = True




def main():
    user_cards = []
    computer_cards = []

    user_total = 0
    computer_total = 0


    user_cards = random.choices(cards, k = 2)
    for card in user_cards:
        user_total += card
    print(f"Your cards: {user_cards}, current score: {user_total}")

    computer_cards = [random.choice(cards)]
    computer_total = sum(computer_cards)
    print(f"Computer's cards: {computer_cards}, second card is hidden.")

    while user_total < 21:  
        hit = input("Type 'y' to hit or 'n' to stand: ").lower()
        if hit == 'y':
            new_card = random.choice(cards)
            user_cards.append(new_card)
            user_total += new_card

        if user_total > 21 and 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                user_total = sum(user_cards)

        print(f"Your cards: {user_cards}, current score: {user_total}")

        if user_total > 21: 
                print("You went over. You lose.")
                return   
        else: 
            break 

    

    
    print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
    while computer_total < 17:
        new_computer_card = random.choice(cards)
        computer_cards.append(new_computer_card)
        computer_total += new_computer_card

        # Handle Ace (11 -> 1) if over 21
        if computer_total > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1
            computer_total = sum(computer_cards)

        print(f"Computer drew: {new_computer_card}. Computer's cards: {computer_cards}, current score: {computer_total}")

    if user_total > 21:
        print("You went over. You lose.")
        return
    elif computer_total > 21:
        print("Computer went over. You win.")
        return

    # Final comparison
    print(f"Final scores -> You: {user_total}, Computer: {computer_total}")
    if user_total > computer_total:
        print("You win!")
    elif user_total < computer_total:
        print("Computer wins!")
    else:
        print("It's a draw.")
    
  

while isActive:
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if continue_game == 'y':
        print(logo)
        main()
    else:
        isActive = False


