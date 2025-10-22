#Write a lambda for map()

#create some employees details
employees = [("Alice", 30, "Albania"), ("Bob", 25, "Bosina"), ("Charlie", 28, "Canada")]

#apply lambda map() to retrive names only

names_employees = list(map(lambda x: x[0], employees))
print(f"People who work here: {names_employees}")

#Bonus: Play around with filter() and reduce() using lambda

employees_above_25 = list(filter(lambda x: x[1] >= 30, employees))
print(f"People who are older than 25 includes {employees_above_25}")

from functools import reduce
total_age = reduce(lambda x, y: x + y[1], employees, 0)
average_age = total_age/len(employees)
print(f"Their average age is {average_age}")
