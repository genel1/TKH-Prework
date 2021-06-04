# Gene Lam
# TKH Pre-work
# Assignment 2

over_under_list = [1,45,32,21,5,17,43,93]
solution = []

# For loop prints out whether each int is under or over 25
for i in over_under_list:
    if i<25:
        solution += ["under"]
        print("under")
    elif i>25: 
        solution += ["over"]
        print("over")
    else:
        solution += ["same"]
        print("same")

# prints out the entire array
print(solution)