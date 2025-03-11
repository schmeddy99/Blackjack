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

    computer_cards = random.choice(cards)
    computer_total += computer_cards
    print(f"Computer's cards: {computer_cards}, computer's score: {computer_total}")

    ## type y to continue n to pass
    hit = input("Type 'y' to hit or 'n' to stand: ").lower()
    if hit == 'y':
        new_card = random.choice(cards)
        user_cards.append(new_card)
        user_total += new_card
        print(f"Your cards: {user_cards}, current score: {user_total}")

    

    ## if y add another card, calculate total
    ## if n reveal computers other card, is less than 17? hit
    ## repeat until > 17 or < 21
    ## compare scores decide winner

while isActive:
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if continue_game == 'y':
        print(logo)
        main()
    else:
        isActive = False
