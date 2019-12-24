direction_dictionary = {"NORTH": "SOUTH",
                        "SOUTH": "NORTH",
                        "EAST": "WEST",
                        "WEST": "EAST"}


def dirReduc(arr):
    temp = arr[:]
    count = 1
    while count:
        count = 0
        for i in range(len(arr) - 1):
            if arr[i + 1] == direction_dictionary[arr[i]]:
                del temp[i + 1]
                del temp[i]
                count = 1
                break
        arr = temp[:]
    return arr


u = ["NORTH", "WEST", "SOUTH", "EAST"]
arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(arr))
print(dirReduc(u))
