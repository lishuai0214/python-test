def str_reverse(str):
    char_list = list(str)
    print(char_list)
    str_len = len(char_list)
    for i in range(0, int(str_len / 2)):
        char_list[i],char_list[str_len-1-i] = char_list[str_len-1-i],char_list[i]

    str = ''.join(char_list)
    return str


if __name__ == '__main__':
    str = "abcdedfg"
    res = str_reverse(str)
    print(res)