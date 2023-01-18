import os
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def generate_starting_cards():
    for i in range(0, 2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))


def score_calculation(cards):
    if sum(cards) > 21:
        card_position = 0
        for card in cards:
            if card == 11:
                cards[card_position] = 1
                card_position += 1
    return sum(cards)


def draw(card_list):
    card_list.append(random.choice(cards))


def who_won():
    user_score = score_calculation(user_cards)
    computer_score = score_calculation(computer_cards)
    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
    if user_score == computer_score:
        print("It's a draw!")
    elif user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose!")


play_game = True

while play_game:
    # on windows
    os.system('cls')
    # on linux / os x
    # os.system('clear')

    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play_blackjack == 'y':
        print(art.logo)

        user_cards = []
        computer_cards = []
        generate_starting_cards()

        print(f"\tYour cards: {user_cards}, current score: {score_calculation(user_cards)}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        while score_calculation(computer_cards) < 17:
            draw(computer_cards)

        draw_more_cards = True

        while draw_more_cards:
            draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if draw_another_card == 'y':
                draw(user_cards)
                print(f"\tYour cards: {user_cards}, current score: {score_calculation(user_cards)}")
                print(f"\tComputer's first card: {computer_cards[0]}")

                if sum(user_cards) > 21:
                    draw_more_cards = False
            else:
                draw_more_cards = False

        who_won()
    else:
        play_game = False