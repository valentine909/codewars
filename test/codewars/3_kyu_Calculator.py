import operator
import re
pattern_addition = re.compile(r"[0-9.,]+\s\+\s[0-9.,]+")
pattern_subtraction = re.compile(r"[0-9.,]+\s\-\s[0-9.,]+")
pattern_multiplication = re.compile(r"[0-9.,]+\s\*\s[0-9.,]+")
pattern_division = re.compile(r"[0-9.,]+\s/\s[0-9.,]+")
pattern_brackets = re.compile(r"\([^\(\)]+\)")
lib = [[pattern_multiplication, ' * ', operator.mul], [pattern_division, ' / ', operator.truediv],
       [pattern_addition, ' + ', operator.add], [pattern_subtraction, ' - ', operator.sub]]


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
    for i in lib:
        while True:
            m = re.findall(i[0], substring)
            if not m:
                break
            else:
                digits = m[0].split(i[1])
                result = i[2](float(digits[0]), float(digits[1]))
                substring = substring.replace(m[0], str(result)).replace('--', '+')
    return substring


a = "((1254 + 3) * 2 / 2 + 3) * (4 + 5) / 6"
b = "1254 + 3 * 2 / 2 + 3 * 4"
c = "2 - 3 - 4 * -5"

p = re.findall(pattern_brackets, a)
print(p)
print(p[0][1:len(p[0]) - 1])

print(eval(b))
print(solve(b))

print(eval(a))
print(find_brackets(a))

print(eval(c))
print(find_brackets(c))

print(c.split(' * '))
