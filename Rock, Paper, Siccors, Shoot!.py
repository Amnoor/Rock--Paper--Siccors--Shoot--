# I am making a game of Rock, Paper, Siccor Shoot!
# First I will import random so it will randomly chooce between Rock, Paper, or Siccor every time the program starts.
import random
# I will assigned a new varible choices with list (the list contains Rock, Paper, and Siccors.).
choices = ["rock", "paper", "siccors"]
# Now using the random that imported I will assign it to program_choice to make the choice between Rock, Paper, or Siccors.
program_choice = random.choice(choices)
# For the start the program will say "Let's play Rock, Paper, Siccors, Shoot!" and "let's start!"
print("Let's play Rock, Paper, Siccors Shoot!")
print("let's start!")
# Then I will ask the user to choose and assign it to a variable users_choice.
users_choice = input("What is your choice (Rock, Paper, Siccors): ")
# If the user inputs "rock", "paper", or "siccors" then the user can proceed with the program, else if they they input something instead of rock, paper, or siccors then the program will print out "Invalid! You can only input rock, paper, or siccors." and ask them again to choose and if they input something other than rock, paper, or siccors then it will repeat until they input rock, paper, or siccors.
if users_choice.lower() == "rock" or users_choice.lower() == "paper" or users_choice.lower() == "siccors":
    pass
else:
    invalid = True
    while invalid:
        print("Invalid! You can only input rock, paper, or siccors.")
        users_choice = input("What is your choice (Rock, Paper, Siccors): ")
        if users_choice.lower() == "rock" or users_choice.lower() == "paper" or users_choice.lower() == "siccors":
            invalid = False
        else:
            pass
# The program will say "Rock," "Paper," "Siccors" "Shoot!" then print out the users answer and the programs answer then depending on who won or loose the program will print out "Congratulations! You've won!" if the user win, else if the user loose then it will print out "You loose!", else if both the program and the user have the same choice then the program will print out "It's a Draw!", and else if some way the user has inputed something other than rock, paper, or siccors than the program will print out "Error!"
print("Rock,")
print("Paper,")
print("Siccors")
print("Shoot!")
print(f"Your answer: {users_choice}")
print(f"My answer: {program_choice}")
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
else:
    print("Error!")