def str_reverse(str):
    char_list = list(str)
    print(char_list)
    str_len = len(char_list)
    for i in range(0, int(str_len / 2)):
        if char_list[i] == 'd':
            char_list[i] = 'W'
        if char_list[str_len-1-i] == 'd':
            char_list[str_len-1-i] = 'W'
        swap(char_list, i, str_len-1-i)

    print("char_list[int(str_len / 2) + 1]:", char_list[int(str_len / 2) ])
    if char_list[int(str_len / 2)] == 'd':
        char_list[int(str_len / 2)] = 'W'

    str = ''.join(char_list)
    return str

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

if __name__ == '__main__':
    str = "abcdedfg"
    res = str_reverse(str)
    print(res)