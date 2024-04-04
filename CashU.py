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


def Money_buckets():
    print("Welcome to money buckets!")
    amount = input("Enter an amount to begin: ")

    blow = amount * 0.6
    grow = amount * 0.2
    mojo = amount * 0.2

    daily = blow * 0.6
    splurge = blow * 0.1
    smile = blow * 0.1
    extinguisher = blow * 0.2

    print("Your blow (60%) is: $" + blow)
    print("Making up your blow is: $")
    print("Daily (60%): $" + daily)
    print("Splurge (10%): $" + splurge)
    print("Smile (10%): $" + smile)
    print("Fire extinguisher (20%): $" + extinguisher)
    print("Your grow (20%) is: $" + grow)
    print("Your mojo (20%) is: $" + mojo)