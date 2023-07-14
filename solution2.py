# Write code for algorithm 2 below

#x will be our end point

def natural_numbers(x, i=1):
	#your code here
    #makes sure that it's a whole number
    if i > x:
        return
    print(i)
    natural_numbers(x, i+1)





natural_numbers(3)
#output: 1 2 3