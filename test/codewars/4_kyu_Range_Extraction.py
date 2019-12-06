"""
https://www.codewars.com/kata/range-extraction/train/python

"""


def solution(args):
    count, start, end = 0, 0, 0
    result = ""
    for i in range(len(args) - 1):  # We're looking for one element further
        if args[i + 1] - args[i] == 1:
            count += 1
        else:  # If numbers are not adjacent do smth based on gathered info
            if count > 1:  # Interval detected
                result += str(start) + "-" + str(end) + ","
            elif count == 1:  # Only two adjacent numbers. That's not interval
                result += str(args[i - 1]) + ","
                result += str(args[i]) + ","
            elif count == 0:  # Standalone number
                result += str(args[i]) + ","
            count, start, end = 0, 0, 0  # Reset
        if count == 1:  # Point on possible start of the interval
            start = args[i]
        elif count > 1:  # Point on possible end of the interval
            end = args[i + 1]
    # Finalizing result when out of the loop
    if start != 0 and end != 0:  # Start and end were pointed before exiting the loop
        result += str(start) + "-" + str(end)
    elif start != 0 and end == 0:  # Only start was pointed
        result += str(args[i]) + "," + str(args[i + 1])
    else:  # Processing the last element of the args
        result += str(args[i + 1])
    return result


b = [17,18,19,20,24,26]
a = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20,24,26]
print(solution(a))

