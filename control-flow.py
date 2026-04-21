def check_letter():
    letter = input("Enter a letter: ")

    # Validate input (must be single letter)
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single letter (a-z or A-Z).")
        return

    # Normalize to lowercase for comp
    letter_lower = letter.lower()

    # Check for vowel or consonant
    if letter_lower in "aeiou":
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


# Call the function
check_letter()