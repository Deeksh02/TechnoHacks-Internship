import random

while True:
    # Display game menu
    print("Welcome to Rock, Paper, Scissors!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    
    # Get user's choice
    choice = int(input("Enter your choice (1-4): "))
    
    # Check if the user wants to quit
    if choice == 4:
        print("Thank you for playing!")
        break
    
    # Generate random choice for the computer
    computer_choice = random.randint(1, 3)
    
    # Print user's choice and computer's choice
    choices = ["Rock", "Paper", "Scissors"]
    print("You chose:", choices[choice - 1])
    print("Computer chose:", choices[computer_choice - 1])
    
    # Determine the winner
    if choice == computer_choice:
        print("It's a tie!")
    elif (choice == 1 and computer_choice == 3) or (choice == 2 and computer_choice == 1) or (choice == 3 and computer_choice == 2):
        print("Congratulations! You win!")
    else:
        print("Sorry, the computer wins!")
    
    print()  # Adding a blank line for readability