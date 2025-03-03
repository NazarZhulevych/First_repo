# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

# Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

# Вимоги до завдання:
# Параметри функції:
# min - мінімальне можливе число у наборі (не менше 1).
# max - максимальне можливе число у наборі (не більше 1000).
# quantity - кількість чисел, які потрібно вибрати (значення між min і max).
# Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
# Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

# Рекомендації для виконання:

# Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
# Використовуйте модуль random для генерації випадкових чисел.
# Використовуйте множину або інший механізм для забезпечення унікальності чисел.
# Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.

import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """Generates a sorted list of unique random numbers within a given range."""
    if quantity > (max_num - min_num + 1):  
        raise ValueError("Quantity cannot be greater than the range of numbers.")

    chosen_numbers = set()  # Use a set to avoid duplicates

    while len(chosen_numbers) < quantity:
        chosen_numbers.add(random.randint(min_num, max_num))

    return sorted(chosen_numbers)  # Return sorted list

# User input with exception handling
try:
    min_number = int(input("Please enter first number of range: ")) 
    max_number = int(input("Please enter last number of range: "))
    quantity_of_numbers = int(input("Please enter amount of returned numbers: "))

    # Ensure valid range
    if min_number > max_number:
        raise ValueError("First number must be smaller than or equal to last number.")

    # Generate and print lottery numbers
    lottery_numbers = get_numbers_ticket(min_number, max_number, quantity_of_numbers)
    print(f"Your lottery numbers: {lottery_numbers}")

except ValueError as e:
    print(f"Error: {e}. Please enter valid numbers.")  # Example: Lottery numbers