from datetime import datetime, date


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        user["birthday"] = user["birthday"].replace("-", ".")
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    users = prepare_user_list(users)
    for user in users:
        user["birthday"] = user["birthday"].replace(year=today.year)
        rest_days = (user["birthday"] - today).days
        if rest_days > 0:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(user["birthday"])})

            
            
    return upcoming_birthdays

users_list = [
    {"name": "Sarah Lee", "birthday": "1957.03.30"},
    {"name": "John Doe", "birthday": "1985.03.28"},
    {"name": "Jane Smith", "birthday": "1990.03.27"},
    {"name": "John Doe", "birthday": "1955-04-23"}, 
]    

for i in get_upcoming_birthdays(users_list):
    print(i)
