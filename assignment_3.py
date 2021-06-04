# Gene Lam
# TKH Pre-work
# Assignment 3

# Loops through a list of names, comparing the length of each name to the
# length of all other names in the list finally printing out only the largest name
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
largest_name_length = -999999999
stored_name = ""
for name in names_list:
    if len(name)>largest_name_length:
        largest_name_length = len(name)
        stored_name = name

# Outputs the largest name and its length
print("The longest name is " + name + " with a length of " + str(largest_name_length) +".")
