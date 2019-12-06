roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
arabian = [1000, 500, 100, 50, 10, 5, 1]


class RomanNumerals:
    pass

    @staticmethod
    def from_roman(roman_number):
        inner_dict = dict(zip(roman, arabian))
        i, result = 0, 0
        while i <= len(roman_number) - 2:
            if inner_dict[roman_number[i]] >= inner_dict[roman_number[i + 1]]:
                result += inner_dict[roman_number[i]]
            else:
                result -= inner_dict[roman_number[i]]
            i += 1
        result += inner_dict[roman_number[i]]  # last number
        return result

    @staticmethod
    def to_roman(arabian_number):
        inner_dict = dict(zip(arabian, roman))
        roman_number = ''
        le = len(str(arabian_number))
        for i in range(le - 1, -1, -1):
            test_number = arabian_number // 10 ** i
            if test_number == 9:
                roman_number += inner_dict[10 ** i] + inner_dict[10 ** (i + 1)]
            elif 5 <= test_number <= 8:
                roman_number += inner_dict[5 * 10 ** i] + inner_dict[10 ** i] * (test_number - 5)
            elif test_number == 4:
                roman_number += inner_dict[10 ** i] + inner_dict[5 * 10 ** i]
            else:
                roman_number += inner_dict[10 ** i] * test_number
            arabian_number %= 10 ** i
        return roman_number


print(RomanNumerals.to_roman(1909))
