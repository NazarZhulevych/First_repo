from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def find_next_weekday(start_date, weekday = 0):
    current_of_week = start_date.weekday()  
    days_ahead = (weekday - current_of_week)%7
    days_ahead = days_ahead if days_ahead > 0 else 7 
    return start_date + timedelta(days=days_ahead)

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        user["birthday"] = str(user["birthday"]).replace("-", ".")
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def adjust_for_weekend(birthday):
    weekday = 0
    if birthday.weekday() >= 5:
        updaet_birthday = find_next_weekday(birthday, weekday)
        return updaet_birthday
    else:
        return birthday

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    users = prepare_user_list(users)
    for user in users:
        user["birthday"] = user["birthday"].replace(year=today.year)
        rest_days = (user["birthday"] - today).days
        if rest_days > 0:
            user["birthday"] = adjust_for_weekend(user["birthday"])
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
