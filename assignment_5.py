# Gene Lam
# TKH Pre-work
# Assignment 5

# Create a function that takes the below list of names, and separates them into two lists one of the names with an even number of letters and one with an odd number of letters.
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

# separates names into even and odd lengths
def separate(name_list):
    even_names = []
    odd_names = []
    for name in name_list:
        if(len(name)%2==0):
            even_names += [name]
        else:
            odd_names += [name]
    # calls another function
    return convert_letter(even_names,'b',odd_names,'c')

# converts a letter in the name depending on whether it is even or odd
def convert_letter(even_list, letter1, odd_list, letter2):
    anotha_even_list = [] 
    anotha_odd_list = []
    for even_name in even_list:
        anotha_even_list += [letter1+even_name[1:]]
    for odd_name in odd_list:
        anotha_odd_list += [odd_name[:len(odd_name)-1]+letter2]
    # Print both lists and then return the even one 
    print(anotha_even_list)
    print(anotha_odd_list)
    return(anotha_even_list)

# return the even one to a variable named even_list and print it again.
even_list = separate(names_list)
print (even_list)