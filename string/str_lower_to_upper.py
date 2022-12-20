def string_lower_to_upper(str):
    res = ''
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            res = res + chr(ord(c) - (ord('a') - ord('A')))
        else:
            res = res + c
    print(res)

if __name__ == '__main__':
    string_lower_to_upper("AbcdEfgE4sc")
    print(ord('x'))
    print(chr(120))