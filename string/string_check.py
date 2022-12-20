
def str_check():
    # 判断字符串是否都是数字字母str.isalnum()
    print('abC12'.isalnum())
    print('ab1#$'.isalnum())

    # 判断字符串是否都是字母str.isalpha()
    print('ab14R'.isalpha())
    print('abYSCcs'.isalpha())

    # 判断字符串是否都是数字str.isdigit()
    print('a1C'.isdigit())
    print('123'.isdigit())

    # 判断字符串是否全为小写str.islower()
    print('ab'.islower())
    print('123'.islower())
    print('Abd'.islower())

    # 判断字符串是否全为大写字母str.isupper()
    print('ab'.isupper())
    print('123'.isupper())
    print('Abd'.isupper())
    print('TCBDEFS'.isupper())

    # 判断字符串首字母是否大写str.istitle()
    print('ab'.istitle())
    print('123'.istitle())
    print('Abd'.istitle())
    print('TCBDEFS'.istitle())


if __name__ == '__main__':
    str_check()