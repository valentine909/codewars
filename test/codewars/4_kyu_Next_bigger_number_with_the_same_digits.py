"""
https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python
1. If number has only 1 digit return -1.
2. If number has digits in increasing order it has a bigger number, else: return -1.
3. Convert number to each digit list.
4. Split the list at digit (named "border") at which increase is observed (first occurrence from the right side).
5. Head is preserved intact.
6. Tail: find the next to border bigger number (named "substitute").
7. Exchange substitute and border in tail. Sort tail.
8. Return concatenated list converted to number.
"""


def next_bigger(n):
    arr = [x for x in str(n)]
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            border, tail, head = arr[i - 1], arr[i:], arr[:i - 1]
            substitute = min([y for y in filter(lambda x: x > border, tail)])
            tail.remove(substitute)
            tail.append(border)
            tail.sort()
            return int(''.join(head+[substitute]+tail))
    return -1


print(next_bigger(80464931186))
print(next_bigger(1))
