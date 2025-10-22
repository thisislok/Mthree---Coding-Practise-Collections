# Your company has organized a morale event! They're hosting a picnic and field day in the park, and of course, they want to play games! Team games! Team building games!

# To do that they want to assign the attendees to certain teams based on their last name. They've already chosen the team names, but they want you to write a program that will sort each person into the correct team.

# Here are the specs:

# If a person's name starts with A, B, C, or D, then they are on the team "Red Dragons"
# If the name starts with E, F, G, or H, they are on the team "Dark Wizards."
# If the name starts with I, J, K, or L, they are on the team "Moving Castles."
# If the name starts with M, N, O, or P, they are on the team "Golden Snitches"
# If the name starts with Q, R, S, or T, they are on the team "Night Guards."
# If the name stars with U, V, W, X, Y, or Z, they are on the team "Black Holes."
# Here's an example of the output:

# What's your last name? Weasley
# Aha! You're on the team "Black Holes"!
# Good luck in the games!
# The example uses the person's last name, but you can choose to use first name if you prefer. You may also use a different output message as long as it clearly states what team the person is on.

name = input("What's your last name?")
name = name.capitalize()

if name[0] in ["A", "B", "C", "D"]:
    print("Aha! You're on the team 'Red Dragons'!\nGood luck in the games!")
elif name[0] in ["E", "F", "G", "H"]:
    print("Aha! You're on the team 'Dark Wizards'!\nGood luck in the games!")
elif name[0] in ["I", "J", "K", "L"]:
    print("Aha! You're on the team 'Moving Castles'!\nGood luck in the games!")
elif name[0] in ["M", "N", "O", "P"]:
    print("Aha! You're on the team 'Golden Snitches'!\nGood luck in the games!")
elif name[0] in ["Q", "R", "S", "T"]:
    print("Aha! You're on the team 'Night Guards'!\nGood luck in the games!")
elif name[0] in ["U", "V", "W", "X", "Y", "Z"]:
    print("Aha! You're on the team 'Black Holes'!\nGood luck in the games!")
else:
    print("Invalid entry!")
