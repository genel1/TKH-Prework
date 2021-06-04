# Gene Lam
# TKH Pre-work
# Assignment 4

def largest_name(names_list):
    largest_name_length = -999999999
    stored_name = ""
    for name in names_list:
        if len(name)>largest_name_length:
            largest_name_length = len(name)
            stored_name = name
    return stored_name

# Input our names_list from assignment 3
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
big_name = largest_name(names_list)
# Outputs the largest name and its length
print("The longest name is " + big_name + " with a length of " + str(len(big_name)) +".")