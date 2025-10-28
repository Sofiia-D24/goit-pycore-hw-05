import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує дійсні числа з тексту, які відокремлені пробілами.
    """
    pattern = r'\b\d+\.\d+\b|\b\d+\b'  # цілі або дробові числа
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable) -> float:
    """
    Підсумовує всі числа, отримані від генератора func.
    """
    return sum(func(text))
