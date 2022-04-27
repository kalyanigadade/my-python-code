while True:
    sentence = input("Enter the sentence:")
    string = sentence.upper()
    print(string)
    count = 0
    list1 = ["a", "e", "i", "o", "u","A","E","I","O","U"]
    for char in string:
        if char in list1:
            count = count+1
    print("number of vowels in given sentence is:",count)
    choice = input("Do you want to continue Y/N::")
    if (choice == "n" or choice == "N"):
        break