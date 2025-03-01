# Спочатку потрібно визначити, який день тижня відповідає start_date. У Python це можна зробити за допомогою методу weekday(), де понеділок = 0, вівторок = 1, і так далі до неділі = 6.
# Потім обчисліть days_ahead, скільки днів залишилося до наступного бажаного дня тижня weekday. Якщо результат виходить меншим або дорівнює 0, це означає, що шуканий день тижня уже минув у цьому тижні, і тому до різниці додається 7, щоб перейти до наступного тижня.
# Потім функція додає обчислену кількість днів days_ahead до start_date, використовуючи timedelta(). Це дає нову дату, яка є наступним weekday після start_date.
# Функція повертає нову дату, яка представляє наступний weekday після start_date.

from datetime import datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

start_date = string_to_date("2024.03.26") 

def find_next_weekday(start_date, weekday = 0):
    current_of_week = start_date.weekday()  
    days_ahead = (weekday - current_of_week)%7
    days_ahead = days_ahead if days_ahead > 0 else 7 
    return start_date + timedelta(days=days_ahead)


start_date = string_to_date("2024.03.26")  # Вівторок
next_monday = find_next_weekday(start_date, 0)  # Наступний понеділок
next_friday = find_next_weekday(start_date, 4)  # Наступна п'ятниця

print(next_monday.strftime("%Y-%m-%d"))  # 2024-04-01
print(next_friday.strftime("%Y-%m-%d"))  # 2024-03-29