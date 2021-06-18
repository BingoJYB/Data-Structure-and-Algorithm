import doctest
import functools
from collections import OrderedDict
from typing import Generator, Dict


ROMAN_ARABIC_PAIR: Dict[str, int] = OrderedDict(
    [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]
)


def connector(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("".join(func(*args, **kwargs)))

    return wrapper


@connector
def convert_arabic_to_roman_numerals(num: int) -> Generator[str, None, None]:
    """
    Convert Arabic number to Roman number.

    >>> convert_arabic_to_roman_numerals(39)
    XXXIX
    >>> convert_arabic_to_roman_numerals(246)
    CCXLVI
    >>> convert_arabic_to_roman_numerals(789)
    DCCLXXXIX
    >>> convert_arabic_to_roman_numerals(1066)
    MLXVI
    >>> convert_arabic_to_roman_numerals(1776)
    MDCCLXXVI
    >>> convert_arabic_to_roman_numerals(1918)
    MCMXVIII
    >>> convert_arabic_to_roman_numerals(2014)
    MMXIV
    >>> convert_arabic_to_roman_numerals(2421)
    MMCDXXI
    """

    for roman, arabic in ROMAN_ARABIC_PAIR.items():
        yield num // arabic * roman
        num %= arabic


if __name__ == "__main__":
    doctest.testmod()
