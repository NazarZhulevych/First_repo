from datetime import datetime


def string_to_date(date_string):
    date_object = datetime.strptime(date_string, "%Y.%m.%d").date()
    return date_object

def date_to_string(date):
    date_object = datetime.strftime(date, "%Y.%m.%d")
    return date_object

date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)
date_string = date_to_string(converted_date)
print(date_string)