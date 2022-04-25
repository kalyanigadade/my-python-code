while True:
    num = int(input("Enter a number: "))
    mod = num % 2
    if mod > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")
    choice=input("Do you want to continue Y/N::")
    if (choice=="n" or  choice == "N"):
      break




