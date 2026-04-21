def weather_advice():
    # Get user input
    cold_input = input("Is it cold? (yes/no): ").strip().lower()
    rain_input = input("Is it raining? (yes/no): ").strip().lower()

    # Convert to boolean val
    is_cold = cold_input == "yes"
    is_raining = rain_input == "yes"

    # Determine advice using logical operators
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")


# Call the function
weather_advice()