import random

computer = random.choice([1, 2, 3])
youStr = input("Enter your choice (S for Snake, W for Water, G for Gun): ")
youDict = {"S": 1, "W": 2, "G": 3}
reverseDict = {1: "Snake", 2: "Water", 3: "Gun"}

# Validate input
if youStr not in youDict:
    print("Invalid input! Please enter 'S', 'W', or 'G'.")
else:
    you = youDict[youStr]
    
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a Draw...!! Play again.")
    else:
        if (computer == 1 and you == 3) or (computer == 2 and you == 1) or (computer == 3 and you == 2):
            print("You Win...!!")
        else:
            print("You Lose.")


