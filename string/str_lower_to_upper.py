
# 第一种办法，用ord和chr转换
def string_lower_to_upper_1(str):
    res = ''
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            res = res + chr(ord(c) - (ord('a') - ord('A')))
        else:
            res = res + c
    print(res)

def string_lower_to_upper_2(str):
    print(str.upper())


if __name__ == '__main__':
    string_lower_to_upper_2("AbcdEfgE4sc")
