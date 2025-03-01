from datetime import datetime, date, timedelta

def string_to_date(date_string):
    """Convert a string (YYYY.MM.DD) to a datetime.date object with leading zeros."""
    date_string = ".".join(f"{int(part):02d}" for part in date_string.split("."))
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date_obj):
    """Convert a datetime.date object to a string (YYYY.MM.DD)."""
    return date_obj.strftime("%Y.%m.%d")

def find_next_weekday(start_date, weekday=0):
    """Find the next occurrence of a specific weekday (default: Monday)."""
    days_ahead = (weekday - start_date.weekday()) % 7
    days_ahead = days_ahead if days_ahead > 0 else 7
    return start_date + timedelta(days=days_ahead)

def prepare_user_list(user_data):
    """Convert users' birthdays from string format to datetime.date format."""
    prepared_list = []
    for user in user_data:
        user["birthday"] = str(user["birthday"]).replace("-", ".")  # Handle different formats
        prepared_list.append({
            "name": user["name"],
            "birthday": string_to_date(user["birthday"])
        })
    return prepared_list

def adjust_for_weekend(birthday):
    """Move birthdays that fall on weekends to the next Monday."""
    if birthday.weekday() >= 5:  # Saturday (5) or Sunday (6)
        return find_next_weekday(birthday, 0)  # Move to next Monday
    return birthday  # Return unchanged if it's a weekday

def get_upcoming_birthdays(users, days=7):
    """Find upcoming birthdays within the next `days` days, adjust for weekends, and move past birthdays to next year."""
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)  # Set birthday to this year

        # If the birthday has already passed this year, move it to the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Adjust if it falls on a weekend
        congratulation_date = adjust_for_weekend(birthday_this_year)
        days_until_birthday = (congratulation_date - today).days  # Days difference

        # Check if within range
        if 0 <= days_until_birthday <= days:
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(congratulation_date)
            })

    return upcoming_birthdays

# User data with corrected formatting
users = [
    {"name": "Bill Gates", "birthday": "1955.06.08"},
    {"name": "Steve Jobs", "birthday": "1955.03.21"},
    {"name": "Jinny Lee", "birthday": "1956.03.22"},
    {"name": "Sarah Lee", "birthday": "1957.03.23"},
    {"name": "Jonny Lee", "birthday": "1958.03.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

# Run the function (example: checking next 365 days)
print(get_upcoming_birthdays(prepare_user_list(users), 365))



