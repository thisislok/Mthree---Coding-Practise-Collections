# Write a script that performs the following steps:

# Collect the following individual pieces of data from the user:
# First name
# Last name
# City where they live
# Their hourly wage
# The number of hours they work each week
# Present the collected information based on the data input in a format like:

# Hi, Firstname Lastname! How are you?
# I hope the weather is nice in City.
# Based on the information you provided, you earn X dollars per week, approximately Y dollars per month, and Z dollars per year.
# Requirements:
# Add your name and the current date in a comment on the first line.
# The user can enter the text values using any case they wish, but the output must have only the first letter of each name and city capitalized.
# For example, if the user enters john, JOHN, or joHn as their first name, the output should be John.
# Assume that there are four weeks in each month, but the yearly calculation should be based on a full year.
# Use correct spelling and punctuation in all user prompts and output.
# Write out the code on your own and verify that it produces the expected outcome and runs without error. Part of testing the program should include making sure that the user can enter their name and city in any case they wish and the output will always use appropriate case.

first_name = input("What's your first name?")
first_name = first_name.capitalize()
last_name = input("Whats your last name?")
last_name = last_name.capitalize()
city = input("What city do you live?")
city = city.capitalize()
hour_wage = float(input("Whats your hour wage?"))
no_of_hour = float(input("How many hours do you work per week?"))

weekly_wage = hour_wage*no_of_hour

wage_list = [(weekly_wage), (weekly_wage*4.2), (weekly_wage*52)]

message = (f"Hi, {first_name} {last_name}! How are you?\nI hope the weather is nice in {city}.\nBased on the information you provided, you earn {wage_list[0]:.1f} dollars per week, approximately {wage_list[1]:.1f} dollars per month, and {wage_list[2]:.1f} dollars per year.")
print(message)
