from datetime import datetime

def get_days_from_today(date) ->int:
    current_date = datetime.now().date()
    date = datetime.strptime(date, "%Y-%m-%d").date()
    days_from_date = (current_date - date).days
    
    return days_from_date

input_date = "2020-10-09"

print(get_days_from_today(input_date))
