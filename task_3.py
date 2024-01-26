def normalize_phone(phone_number):
    import re

    phone_number = re.sub(r"[^0-9]", "", phone_number) # Only numbers in phone_number
    
    if len(phone_number) == 10:
        phone_number = "38" + phone_number
    phone_number = "+" + phone_number  

    return phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
