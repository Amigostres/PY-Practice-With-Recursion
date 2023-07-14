# Write code for algorithm 1 below
def count_down(n):

    #base case
    if n==0 or n < 0:
        print("it's done")
        return 
    
    #recursive case
    else:
        print(n)
        count_down(n-1)

count_down(10)