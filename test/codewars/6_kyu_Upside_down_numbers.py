"""
https://www.codewars.com/kata/upside-down-numbers/train/python
1. Make dict. 2. Convert to string. 3. Rotate. 4. Check.
"""

rotate_dict = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}


def solve(a, b):
    count = 0
    for i in range(a, b):
        rotated = ""
        for j in str(i)[::-1]:
            if j in rotate_dict:
                rotated += rotate_dict[j]
            else:
                break
        if rotated == str(i):
            count += 1
    return count


print(solve(0, 10))
print(solve(100, 1000))
