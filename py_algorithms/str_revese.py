def str_reverse(str):
    char_list = list(str)
    print(char_list)
    str_len = len(char_list)
    for i in range(0, int(str_len // 2)):
        char_list[i],char_list[str_len-1-i] = char_list[str_len-1-i],char_list[i]

    str = ''.join(char_list)
    return str

def str_reverse_1(str):
    str_arr = list(str)
    print(str_arr)
    for i in range(len(str_arr)//2):
        str_arr[i], str_arr[len(str_arr)-i-1] = str_arr[len(str_arr)-i-1], str_arr[i]
    return "".join(str_arr)

if __name__ == '__main__':
    str = "abcdedfg"
    res = str_reverse_1(str)
    print(res)