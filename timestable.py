def timestable(n):
    for row in range(1,n+1):
        for column in range(1,n+1):
            grid = print(row*column,end='\t')
        space = print()
    return(grid)   
    return(space)
        

n = int(input("Please enter a number: "))
(timestable(n))
