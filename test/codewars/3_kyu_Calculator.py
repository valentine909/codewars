import operator
import re
pattern_addition = re.compile(r"\-?[0-9.,]+\s\+\s\-?[0-9.,]+")
pattern_subtraction = re.compile(r"\-?[0-9.,]+\s\-\s\-?[0-9.,]+")
pattern_multiplication = re.compile(r"\-?[0-9.,]+\s\*\s\-?[0-9.,]+")
pattern_division = re.compile(r"\-?[0-9.,]+\s/\s\-?[0-9.,]+")
pattern_brackets = re.compile(r"\([^\(\)]+\)")
lib1 = {"*": [pattern_multiplication, ' * ', operator.mul], "/": [pattern_division, ' / ', operator.truediv]}
lib2 = {"+": [pattern_addition, ' + ', operator.add], "-": [pattern_subtraction, ' - ', operator.sub]}
libs = [lib1, lib2]


class Calculator(object):
  def evaluate(self, string):
    return float(find_brackets(string))


def find_brackets(string):
    m = re.findall(pattern_brackets, string)
    for i in m:
        result = solve(i[1:len(i) - 1])
        string = string.replace(i, str(result)).replace('--', '+')
    if m:
        string = find_brackets(string)
    else:
        return solve(string)
    return string


def solve(substring):
    for lib in libs:
        for i in substring:
            if i in lib:
                while True:
                    m = re.findall(lib[i][0], substring)
                    if not m:
                        break
                    else:
                        digits = m[0].split(lib[i][1])
                        result = lib[i][2](float(digits[0]), float(digits[1]))
                        substring = substring.replace(m[0], str(result)).replace('--', '+')
    return substring


a = "((1254 + 3) * 2 / 2 + 3) * (4 + 5) / 6"
b = "1254 + 3 * 2 / 2 + 3 * 4"
c = "2 - 3 - 4 * -5"
d = "2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"

print(eval(b))
print(solve(b))

print(eval(a))
print(find_brackets(a))

print(eval(c))
print(find_brackets(c))

print(eval(d))
print(find_brackets(d))
