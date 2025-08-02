import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

blackjack = input("Do you want to play Black Jack? 'y' to continue or 'n' to quit: ")

if blackjack == "y":
    user = random.sample(cards, 2)
    computer = random.sample(cards, 2)

    user_cards = user
    computer_cards = computer

    print(f"The user cards are: {user_cards}\nThe computer's first card is: {computer_cards[0]}")

    x = sum(user_cards)
    y = sum(computer_cards)

    def the_highest(x, y):
        if x > y and x <= 21:
            print("You win!")
        elif y > x and y <= 21:
            print("Computer wins!")
        elif x > 21:
            print("You busted! Computer wins.")
        elif y > 21:
            print("Computer busted! You win.")
        else:
            print("It's a draw!")

    def check(x, y):
        again = input("Type 'y' to get another card, or 'n' to pass: ")

        if again == "y":
            new_card = random.choice(cards)
            user_cards.append(new_card)
            x = sum(user_cards)

            print(f"Your new cards: {user_cards} (Total: {x})")

            if x > 21:
                print("You busted! Computer wins.")
                return

            while y < 17:  
                new_computer_card = random.choice(cards)
                computer_cards.append(new_computer_card)
                y = sum(computer_cards)

            print(f"Computer's cards: {computer_cards} (Total: {y})")
            the_highest(x, y)
        else:
           while y < 17:  
               new_computer_card = random.choice(cards)
               computer_cards.append(new_computer_card)
               y = sum(computer_cards)

               print(f"Computer's final cards: {computer_cards} (Total: {y})")
               the_highest(x, y)

    check(x, y)

else:
    print("Okay, have a nice day!")
