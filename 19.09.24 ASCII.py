
ASCII_dict = {
    'А': '11000000', 'Б': '11000001', 'В': '11000010', 'Г': '11000011',
    'Д': '11000100', 'Е': '11000101', 'Ж': '11000110', 'З': '11000111',
    'И': '11001000', 'Й': '11001001', 'К': '11001010', 'Л': '11001011',
    'М': '11001100', 'Н': '11001101', 'О': '11001110', 'П': '11001111',
    'Р': '11010000', 'С': '11010001', 'Т': '11010010', 'У': '11010011',
    'Ф': '11010100', 'Х': '11010101', 'Ц': '11010110', 'Ч': '11010111',
    'Ш': '11011000', 'Щ': '11011001', 'Ъ': '11011010', 'Ы': '11011011',
    'Ь': '11011100', 'Э': '11011101', 'Ю': '11011110', 'Я': '11011111',
    'а': '11100000', 'б': '11100001', 'в': '11100010', 'г': '11100011',
    'д': '11100100', 'е': '11100101', 'ж': '11100110', 'з': '11100111',
    'и': '11101000', 'й': '11101001', 'к': '11101010', 'л': '11101011',
    'м': '11101100', 'н': '11101101', 'о': '11101110', 'п': '11101111',
    'р': '11110000', 'с': '11110001', 'т': '11110010', 'у': '11110011',
    'ф': '11110100', 'х': '11110101', 'ц': '11110110', 'ч': '11110111',
    'ш': '11111000', 'щ': '11111001', 'ъ': '11111010', 'ы': '11111011',
    'ь': '11111100', 'э': '11111101', 'ю': '11111110', 'я': '11111111',
    'Ё': '10101010', 'ё': '10101110',
    ' ': '10100000',  # Пробел
    ',': '10000010',  # Запятая
    '.': '00101110'   # Точка
}

# Исходная строка
input_string = "Смотрите на звёзды, но крепко стойте на ногах."

# Закодированная строка в виде списка двоичных кодов
encoded_string = ''.join([ASCII_dict.get(char, '') for char in input_string])

# Разделяем строку на части по 8 символов с пробелами
encoded_string_with_spaces = ' '.join([encoded_string[i:i+8] for i in range(0, len(encoded_string), 8)])

# Выводим результат
print(f"Закодированная строка в двоичном виде с пробелами: {encoded_string_with_spaces}")
