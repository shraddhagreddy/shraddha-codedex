import random

# Prompt user
player = int(input("Enter a number (1 = Rock ✊, 2 = Paper ✋, 3 = Scissors ✌️): "))

# Computer randomly chooses 1–3
computer = random.randint(1, 3)

# Display choices
choices = {1: "Rock ✊", 2: "Paper ✋", 3: "Scissors ✌️"}
print(f"You chose: {choices[player]}")
print(f"Computer chose: {choices[computer]}")

# Determine winner using control flow
if player == computer:
    print("It's a tie!")
elif (player == 1 and computer == 3) or \
     (player == 2 and computer == 1) or \
     (player == 3 and computer == 2):
    print("You win! 🎉")
else:
    print("Computer wins! 💻")
