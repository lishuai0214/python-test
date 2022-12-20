def str_print():
    str = '这是一句话'
    print(str)
    str = "What's your name?"
    print(str)
    str ='''
    这是一个多行文本. 这是第一行.这是第二行.
    "你的名字是," 我问到。他会答"我的名字是木木"
    '''
    print(str)

def str_join():
    strings = ['do', 're', 'mi']
    res = "_".join(strings)
    print(res)


#重复输出字符串
def str_x():
    str = "string"
    print(str*2)

#通过索引获取字符串中字符
def str_index():
    str = "string"
    print(str[0])
    print(type(str[0]))
    
    s = 'ABCDEFGHIJKLMN'
    s1 = s[0]
    print('s[0] = ' + s1)  # s[0] = A
    print('s[3] = ' + s[3])  # s[3] = D
    print('倒数第三个数为：' + s[-3])  # 倒数第三个数为：L
    print('最后一个数为：' + s[-1])  # 最后一个数为：N


#截取字符串中的一部分
def str_cut():
    str = "string"
    print(str[-3: ])

#成员运算符
def str_in():
    str = "string"
    print('i' in str)
    print('k' in str)

def str_revese():
    a = '123456789'
    print(a[::-1])


if __name__ == '__main__':
    # str_cut()
    dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    print(dic)