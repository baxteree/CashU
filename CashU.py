def __main__():
    print("Welcome to 'CashU'!")

    # Get an input for what function the user wants to run
    choice = input("Enter [1] for money buckets, \nEnter [2] for compound interest: ")

    # While the input is not blank:
    while choice:
        if int(choice) == 1:
            # Run the money buckets function if the user inputs 1
            money_buckets()

        elif int(choice) == 2:
            # Run the compound interest function if the user inputs 2
            compound_interest()

        else:
            # Print this if the user doesn't input 1 or 2
            print("Not a valid input!")

        # After the functions have been run, or the user didn't input correctly,
        # repeat the functions by grabbing more input until the user enters blank.
        print("----------------------------")
        print("Enter nothing to exit.")
        choice = input("Enter [1] for money buckets, \nEnter [2] for compound interest: ")


def money_buckets():
    print("Welcome to money buckets!")

    # The amount that the money buckets will be calculated by
    amount = int(input("Enter an amount to begin: "))

    # Calculate the different amounts for the parts of the buckets
    blow = amount * 0.6
    grow = amount * 0.2
    mojo = amount * 0.2

    daily = blow * 0.6
    splurge = blow * 0.1
    smile = blow * 0.1
    extinguisher = blow * 0.2

    # Print the different amounts for the parts of the buckets
    print(f"Your blow (60%) is: ${blow}")
    print("Making up your blow is:")
    print(f"Daily (60%): ${daily}")
    print(f"Splurge (10%): ${splurge}")
    print(f"Smile (10%): ${smile}")
    print(f"Fire extinguisher (20%): ${extinguisher}")
    print(f"Your grow (20%) is: ${grow}")
    print(f"Your mojo (20%) is: ${mojo}")


def compound_interest():
    print("Welcome to the miracle of compound interest!")

    # The age that the user will start their investments on
    age = int(input("Enter your starting age: "))

    # If the age is not within 0-60, enter this loop
    while not 0 <= age <= 60:
        # Tell the user that they inputted an invalid age,
        # and ask them to input age again.
        print("Invalid age: please pick between 0 - 60.")
        age = int(input("Enter your starting age: "))

    # The amount that the user will invest each year
    amount = int(input("Enter the amount you'll invest each year: "))

    # The annual interest rate
    rate = int(input("Enter the annual interest rate (do not add % sign): "))

    # Setting the total amount of money that the user has to 0
    total = 0

    # Print the top line of the table
    print("Age -- You invest -- Total")

    # For each age until age is 60:
    for i in range(age, 61):
        # The amount invested each year is added to the current total
        total += amount
        # The interest rate is added on top of the current total
        total += total * rate / 100

        # Round the total to a whole number
        total = int(round(total, 0))

        # Print each line of the table
        print(f"{i} -- ${amount} -- ${total}")


__main__()
