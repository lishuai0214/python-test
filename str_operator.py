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

#截取字符串中的一部分
def str_cut():
    str = "string"
    print(str[0: 3])

#成员运算符
def str_in():
    str = "string"
    print('i' in str)
    print('k' in str)

if __name__ == '__main__':
    str_in()