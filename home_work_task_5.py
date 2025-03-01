from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    weekday = 0
    if birthday.weekday() >= 5:
        updaet_birthday = find_next_weekday(birthday, weekday)
        return updaet_birthday
    else:
        return birthday
