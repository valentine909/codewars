"""
https://www.codewars.com/kata/nesting-structure-comparison/train/python
1. Convert to text.
2. Omit any digits, spaces and brackets.
3. Compare strings.
4. Profit!
"""


def same_structure_as(original, other):
    import re
    patterns = []
    a = str(original)
    b = str(other)
    patterns.append((re.compile('\'\]\''), ''))
    patterns.append((re.compile('\'\[\''), ''))
    patterns.append((re.compile('[\d\s]'), ''))
    for p in patterns:
        a = re.sub(p[0], p[1], a)
        b = re.sub(p[0], p[1], b)
    print(a)
    print(b)
    return a == b


print(same_structure_as([1,[1,1]],[2,[2,2]]))
print(same_structure_as([1,[1,1]],[[2,2],2]))
print(same_structure_as([1,'[',']'],['[',']',1]))