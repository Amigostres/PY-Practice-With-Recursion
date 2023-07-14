# Write code for algorithm 3 below
def fibonacho(n):
    if n== 2:
      return 1  
    if n == 1:
        return 0
    
    print(n,n-1, n-2)
    return fibonacho(n-1) + fibonacho(n-2)

print(fibonacho(10))