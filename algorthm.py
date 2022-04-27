while True:
    num1=int(input("enter number of rows needed:"))
    n=1
    while n<=num1:
            print("Square of",n,"is",n*n)
            n=n+1
    choice = input("Do you want to continue Y/N::")
    if (choice == "n" or choice == "N"):
            break