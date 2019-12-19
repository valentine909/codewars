import re
pattern_addition = re.compile(r"\d+\s\+\s\d+")
pattern_subtraction = re.compile(r"\d+\s\-\s\d+")
pattern_multiplication = re.compile(r"\d+\s\*\s\d+")
pattern_division = re.compile(r"\d+\s/\s\d+")
pattern_brackets = re.compile(r"\([^\(\)]+\)")


class Calculator(object):
  def evaluate(self, string):
    return 0


a = "((1254 + 3) * 2 / 2 + 3) * (4 + 5) / 6"
b = "1254 + 3 * 2 / 2 + 3 * 4"


def find_brackets(string):
    m = re.findall(pattern_brackets, string)
    for i in m:
        a = solve(m[0][1:len(m[0]) - 1])
    if m:
        find_brackets(string)


def solve(substring):
    if '/' in substring:
        digits = substring.split(" / ")
    print(float(digits[0]) / float(digits[1]))



p = re.findall(pattern_brackets, a)
print(p[0][1:len(p[0]) - 1])

solve("2 / 5")
