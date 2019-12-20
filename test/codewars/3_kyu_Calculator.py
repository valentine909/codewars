import operator
import re
# Operation patterns assume to find positive or negative integer or float numbers to the left
# and to the right of the corresponding operator. Applied consequently form left to right
pattern_addition = re.compile(r"\-?[0-9.,]+\s\+\s\-?[0-9.,]+")
pattern_subtraction = re.compile(r"\-?[0-9.,]+\s\-\s\-?[0-9.,]+")
pattern_multiplication = re.compile(r"\-?[0-9.,]+\s\*\s\-?[0-9.,]+")
pattern_division = re.compile(r"\-?[0-9.,]+\s/\s\-?[0-9.,]+")
# Find everything in brackets that doesn't contain nesting brackets. Applied recursively
pattern_brackets = re.compile(r"\([^\(\)]+\)")
# Libs for DRY code
lib1 = {"*": [pattern_multiplication, ' * ', operator.mul], "/": [pattern_division, ' / ', operator.truediv]}
lib2 = {"+": [pattern_addition, ' + ', operator.add], "-": [pattern_subtraction, ' - ', operator.sub]}
libs = [lib1, lib2]


class Calculator(object):
    def evaluate(self, string):
        return float(find_brackets(string))  # Start with finding brackets


def find_brackets(string):
    m = re.findall(pattern_brackets, string)
    for i in m:
        result = solve(i[1:len(i) - 1])  # Omit bordering brackets in 'solve' argument
        string = string.replace(i, str(result))
    if m:
        string = find_brackets(string)  # Check if there are more brackets
    else:
        return solve(string)
    return string


def solve(substring):
    for lib in libs:  # Multiplication and division first, addition and subtraction second
        i = 1  # If string starts from 'minus'
        while i < len(substring):
            if substring[i] in lib:
                j = substring[i]  # To shorten code lines
                m = re.findall(lib[j][0], substring)  # Apply pattern
                digits = m[0].split(lib[j][1])  # Get splitting symbol
                result = lib[j][2](float(digits[0]), float(digits[1]))  # Applying operator
                substring = substring.replace(m[0], str(result))
                i = 1  # Start over again after string modification
            else:
                i += 1
    return substring


if __name__ == '__main__':
    tmp = Calculator()
    a = "((1254 + 3) * 2 / 2 + 3) * (4 + 5) / 6"
    b = "1254 + 3 * 2 / 2 + 3 * 4"
    c = "2 - 3 - 4 * -5"
    d = "2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"
    e = "-2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"
    examples = [b, a, c, d, e]
    for i in examples:
        print(eval(i), ' vs. ', tmp.evaluate(i), end='\n\n')
