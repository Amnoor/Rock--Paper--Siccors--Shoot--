# Rock, Paper, Siccors, Shoot!
# A simple game of rock, paper, siccors against the computer.
# First I will import the choice function from the random module.
from random import choice
# Then I will create a list of choices for the computer to choose from.
choices = ["rock", "paper", "siccors"]
# Then I will use the random.choice() function to select a random choice from the list.
program_choice = choice(choices)
# Then I will print a welcome message and ask the user for their choice.
print("Let's play Rock, Paper, Siccors Shoot!")
print("let's start!")
users_choice = input("What is your choice (Rock, Paper, Siccors): ")
# Then I will use a match-case statement to check if the user's input is valid.
match users_choice.lower():
    case "rock" | "paper" | "siccors":
        pass
    case _:
        invalid = True
        while invalid:
            print("Invalid! You can only input rock, paper, or siccors.")
            users_choice = input("What is your choice (Rock, Paper, Siccors): ")
            if users_choice.lower() == "rock" or users_choice.lower() == "paper" or users_choice.lower() == "siccors":
                invalid = False
            else:
                pass
# Then I will print Rock, Paper, Siccors, Shoot! and the choices of both the user and the computer.
print("Rock,")
print("Paper,")
print("Siccors")
print("Shoot!")
print(f"Your answer: {users_choice}")
print(f"My answer: {program_choice}")
# Finally, I will use if-elif-else statements to determine the winner and print the result.
if program_choice.lower() == users_choice.lower():
    print("It's a Draw!")
elif program_choice.lower() == "rock" and users_choice.lower() == "paper":
    print("Congratulations! You've won!")
elif program_choice.lower() == "rock" and users_choice.lower() == "siccors":
    print("You loose!")
elif program_choice.lower() == "paper" and users_choice.lower() == "siccors":
    print("Congratulations! You've won!")
elif program_choice.lower() == "paper" and users_choice.lower() == "rock":
    print("You loose!")
elif program_choice.lower() == "siccors" and users_choice.lower() == "rock":
    print("Congratulations! You've won!")
elif program_choice.lower() == "siccors" and users_choice.lower() == "paper":
    print("You loose!")
# Just in case something goes wrong, I will add an else statement to catch any errors.
else:
    print("Error!")