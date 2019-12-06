"""
https://www.codewars.com/kata/roman-numerals-helper/train/python
to_roman method based on floor division
from_roman method sums up numbers gained from dictionary. For reversed numbers such as 'CM' or 'CD' the fist
numbers then is subtracted twice.
"""


class RomanNumerals:
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabian = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    @classmethod
    def from_roman(cls, roman_number):
        inner_dict = dict(zip(RomanNumerals.roman, RomanNumerals.arabian))
        result = sum([inner_dict[i] for i in roman_number])
        for i in range(1, len(roman_number)):
            if inner_dict[roman_number[i - 1]] < inner_dict[roman_number[i]]:
                result -= inner_dict[roman_number[i - 1]] * 2
        return result

    @classmethod
    def to_roman(cls, arabian_number):
        roman_number = ''
        for index, item in enumerate(RomanNumerals.arabian):
            roman_number += RomanNumerals.roman[index] * (arabian_number // item)
            arabian_number %= item
        return roman_number


print(RomanNumerals.to_roman(4))
print(RomanNumerals.from_roman('MCMXC'))
print(RomanNumerals.to_roman(1909))
print(RomanNumerals.from_roman('IV'))
