from typing import Counter


def hammingWeight(n: int) -> int:

    # Переводим в битовую строку
    bits = bin(n)

    # Создаем Counter
    counter = Counter(bits)

    # Возврашаем 1
    return counter["1"]


print(hammingWeight(11))  # 3
