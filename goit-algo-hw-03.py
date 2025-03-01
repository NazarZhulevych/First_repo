from datetime import datetime

def get_days_from_today(date: str) ->int:
    try:
        current_date = datetime.now().date()
        date = datetime.strptime(date, "%Y-%m-%d").date()
        days_from_date = (current_date - date).days
        return days_from_date
    except ValueError:
        print("Помилка: Неправильний формат дати! Використовуйте YYYY-MM-DD.")
        return None
    

input_date = input("Введіть дату у форматі YYYY-MM-DD, (наприклад: 2012-12-12) :")

print(f"Кількість днів між заданою датою і поточною датою: {get_days_from_today(input_date)}")
