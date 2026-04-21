def determine_season():
    # Get user input
    month = input("Enter the month of the year (Jan - Dec): ").strip().title()
    
    try:
        day = int(input("Enter the day of the month: "))
    except ValueError:
        print("Invalid day. Please enter a number.")
        return

    # Validate month
    valid_months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    
    if month not in valid_months:
        print("Invalid month. Please enter a valid three-letter month (Jan - Dec).")
        return

    # Validate day
    if day < 1 or day > 31:
        print("Invalid day. Please enter a valid day (1–31).")
        return

    # Determine season
    if (month == "Dec" and day >= 21) or month in ("Jan", "Feb") or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or month in ("Apr", "May") or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or month in ("Jul", "Aug") or (month == "Sep" and day <= 21):
        season = "Summer"
    else:
        season = "Fall"

    # Output result
    print(f"{month} {day} is in {season}.")


# Call the function
determine_season()