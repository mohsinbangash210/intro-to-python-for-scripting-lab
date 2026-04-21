def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))

        # Validate input
        if age < 0:
            print("Invalid input. Age cannot be negative.")
            return

        # Calculate dog years
        if age <= 2:
            dog_years = age * 10
        else:
            dog_years = (2 * 10) + ((age - 2) * 7)

        # Output result
        print(f"The dog's age in dog years is {dog_years}.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Call the function
calculate_dog_years()