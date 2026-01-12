def Number_guessing_game():
    
    import random
    computer = random.randint(1, 100)
    chances_taken = 0
    while chances_taken < 10:
        user_input = int(input("Enter your guessed number :"))
        chances_taken += 1
        remaining_chances = 10 - chances_taken
            
        if user_input == computer:
            print("You win.")
            break
        else:
            print(f"Computer wins and there are only {remaining_chances} chances left.")
                
            if user_input > computer:
                print("Hint:The number that you guessed is greater than the correct answer.")
                    
            else:
                print("Hint:The number that you guessed is lower than the correct answer.")
                    
            if user_input != computer and chances_taken == 10:
                print(f"You lose the game !! try again later and the correct answer is {computer}.")

Number_guessing_game()
