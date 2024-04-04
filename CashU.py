def __main__():
    print("Welcome to 'CashU'!")

    choice = input("Enter [1] for money buckets, \nEnter [2] for compound interest: ")

    while choice:
        if int(choice) == 1:
            Money_buckets()

        elif int(choice) == 2:
            Compound_interest()

        else:
            print("Not a valid input!")

        print("----------------------------")
        print("Enter nothing to exit.")
        choice = input("Enter [1] for money buckets, \nEnter [2] for compound interest: ")


def Money_buckets():
    print("Welcome to money buckets!")
    amount = int(input("Enter an amount to begin: "))

    blow = amount * 0.6
    grow = amount * 0.2
    mojo = amount * 0.2

    daily = blow * 0.6
    splurge = blow * 0.1
    smile = blow * 0.1
    extinguisher = blow * 0.2

    print(f"Your blow (60%) is: ${blow}")
    print("Making up your blow is:")
    print(f"Daily (60%): ${daily}")
    print(f"Splurge (10%): ${splurge}")
    print(f"Smile (10%): ${smile}")
    print(f"Fire extinguisher (20%): ${extinguisher}")
    print(f"Your grow (20%) is: ${grow}")
    print(f"Your mojo (20%) is: ${mojo}")


def Compound_interest():
    print("Welcome to the miracle of compound interest!")

    age = int(input("Enter your starting age: "))

    while age > 60 and age < 0:
        print("Invalid age: please pick between 0 - 60.")
        age = int(input("Enter your starting age: "))

    amount = int(input("Enter the amount you'll invest each year: "))
    rate = int(input("Enter the annual interest rate (do not add % sign): "))

    total = 0

    print("Age -- You invest -- Total")

    for i in range(age, 61):
        total += amount
        total += total * rate / 100

        total = int(total)

        print(f"{i} -- ${amount} -- ${total}")


__main__()