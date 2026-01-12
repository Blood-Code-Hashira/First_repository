def password_manager():
    
    password = int(input("Enter your password :"))
    chances_taken = 0
    
    while chances_taken < 5:
        user_input = int(input("Enter your password :"))
        chances_taken += 1
        remaining_chances = 5 - chances_taken
        
        if user_input == password:
            print("You entered the correct password.")
            break
        else:
            print(f"You entered the incorrect password and there are only {remaining_chances} chances left.")
            
        if user_input != password and chances_taken == 5:
            print("Too many attempts !!.\nTry again later.")
            
password_manager()
    