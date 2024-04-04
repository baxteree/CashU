print("Welcome to 'CashU'!")

choice = int(input("Enter [1] for money buckets, \nEnter [2] for compound interest: "))

while choice != "":
    if choice == 1:
        Money_buckets()

    elif choice == 2:
        Compound_interest()

    else:
        print("Not a valid input!")

    print("----------------------------")
    print("Enter nothing to exit.")
    choice = int(input("Enter [1] for money buckets, \nEnter [2] for compound interest: "))


