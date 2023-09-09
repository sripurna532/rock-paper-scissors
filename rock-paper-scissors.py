rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

gestures = [rock, paper, scissors]
user_index = int(input("What will you select,rock(0),paper(1) or scissors(2)\n"))
print("\nYou Select:")
print(gestures[user_index])

print("Computer Selects:")
computer_index = random.randint(0, 2)
print(gestures[computer_index])

if (
    (user_index == 0 and computer_index == 2)
    or (user_index == 1 and computer_index == 0)
    or (user_index == 2 and computer_index == 1)
):
    print("You win")
elif user_index == computer_index:
    print("Draw")
else:
    print("Computer Win")
