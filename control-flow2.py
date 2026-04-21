def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))

        # Validate age
        if age < 0:
            print("Invalid input. Age cannot be negative.")
            return

        voting_age = 18  # minimum voting age

        # Check eligibility
        if age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote yet.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Call the function
check_voting_eligibility()