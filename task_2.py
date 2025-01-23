#  Генератор случайных паролей

import random
import string

chars = string.ascii_letters + string.digits
password = ''.join(random.choices(chars, k=8)) # ''.join Объединяет выбранные символы в одну строку, чтобы получить пароль.
print(password)
