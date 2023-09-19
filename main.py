# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    flag = arr[len(arr)//2]

    left = [x for x in arr if x < flag]
    mid = [x for x in arr if x == flag]
    right = [x for x in arr if x > flag]

    return quick_sort(left) + mid + quick_sort(right)


def quick_sort_1(arr):
    if len(arr) <= 1:
        return arr
    flag = len(arr)//2

    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] < flag:
            arr[left], arr[flag] = arr[flag], arr[left]
            flag = left
            left = left + 1



def print_hi(name):
    a = {"key": "vale"}
    b = a
    b["key2"] = "value2"
    print(a)
    print(b)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [10, 9, 4, 3, 6, 7, 3, 4]
    [6, 9, 4, 3, 10, 7, 3, 4]
    print(quick_sort(arr))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
