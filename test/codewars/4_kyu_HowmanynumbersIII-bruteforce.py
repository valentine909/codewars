def dig(power, digit):
    if power == 1:
        return [[i for i in range(digit, 10, 1)], [i for i in range(digit, 10, 1)]]
    else:
        k = [[], []]
        for i in range(digit, 10, 1):
            k[0] += [x + i * 10 ** (power - 1) for x in dig(power - 1, i)[0]]
            k[1] += [y + i for y in dig(power - 1, i)[1]]
        return k


def find_all(sum_dig, digs):
    results = []
    data = dig(digs, 1)
    for index, number in enumerate(data[1]):
        if number == sum_dig:
            results.append(data[0][index])
    le = len(results)
    print(results)
    if le == 0:
        return []
    return [le, results[0], results[-1]]


print(find_all(35, 6))
# print(dig(3, 1))
