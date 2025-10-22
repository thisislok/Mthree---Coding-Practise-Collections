# Write a program that will calculate the cost of a custom cup of coffee at a gourmet coffee shop, based on the size of the cup, the type of coffee selected, and flavors that can be added to the coffee. It should complete the following steps:

# Ask the user what size cup they want, choosing between small, medium, and large.
# Ask the user what kind of coffee they want, choosing between brewed, espresso, and cold brew.
# Ask the user what flavoring they want, if any. Choices include hazelnut, vanilla, and caramel.
# Calculate the price of the cup using the following values:
# Size:
# small: $2
# medium: $3
# large: $4
# Type:
# brewed: no additional cost
# espresso: 50 cents
# cold brew: $1
# Flavoring:
# None: no additional cost
# All other options: 50 cents
# Display a statement that summarizes what the user ordered.
# Display the total cost of the cup of coffee as well as the cost with a 15% tip, in phrases that explain the values to the user. Round the cost with tip to two decimal places.
# For example, if the user asks for a medium-sized espresso with hazelnut flavoring, the total should be $4; the total with a tip should be $4.60.
# Sample Output
# Here is an example of what the user might see when they run this program:

# Do you want small, medium, or large? small
# Do you want brewed, espresso, or cold press? espresso
# Do you want a flavored syrup? (Yes or No) yes
# Do you want hazelnut, vanilla, or caramel? vanilla
# You asked for a small cup of espresso coffee with vanilla syrup.
# Your cup of coffee costs 3.0
# The price with a tip is 3.45
# Tips
# Build the program one condition at a time, checking that each condition works as expected before adding the next condition.
# Include the user's options in the prompt, so the user knows what values are acceptable answers to each question.
# Test all possible answers to make sure they work and produce the expected outcome.

size = [(1, "Small", 2), (2, "Medium", 3), (3, "Large", 4)]
type = [(1, "Brewed", 0), (2, "Espresso", 0.5), (3, "Cold Brew", 1)]
flv = [(1, "None", 0), (2, "Chocolate", 0.5), (3, "Vanilla", 0.5)]
cost = 0
order_name = []

order_size = int(input(f"Press {size[0][0]} for {size[0][1]}\nPress {size[1][0]} for {size[1][1]}\nPress {size[2][0]} for {size[2][1]}\n Enter:"))

for digit in size:
    if order_size == digit[0]:
        cost += float(digit[2])
        order_name.append(digit[1])
        break

order_type = int(input(f"Press {type[0][0]} for {type[0][1]}\nPress {type[1][0]} for {type[1][1]}\nPress {type[2][0]} for {type[2][1]}\n Enter:"))

for digit in type:
    if order_type == digit[0]:
        cost += float(digit[2])
        order_name.append(digit[1])
        break

order_flv = int(input(f"Press {flv[0][0]} for {flv[0][1]}\nPress {flv[1][0]} for {flv[1][1]}\nPress {flv[2][0]} for {flv[2][1]}\n Enter:"))

for digit in flv:
    if order_flv == digit[0]:
        cost += float(digit[2])
        order_name.append(digit[1])
        break

with_tip = cost*1.15
print(f"Your order is: {order_name}")
print(f"The total is: £{cost}\nand with tip is: £{with_tip:.2f}")
