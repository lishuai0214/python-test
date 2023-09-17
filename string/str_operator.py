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

    # 格式化字符串输出
    var1 = 'str1'
    var2 = 'str2'
    print(f'str: {var1}, str: {var2}')
    print('str: {}, str: {}'.format(var1, var2))

def str_join():
    strings = ['do', 're', 'mi']
    res = "_".join(strings)
    print(res)


#len()：返回字符串的长度。
def str_len():
    text = "Hello, World!"
    length = len(text)  # 返回 13
    print(length)

#str()：将其他数据类型转换为字符串。
def str_str():
    num = 42
    text = str(num)  # 返回 "42"
    print(text)

#concatenation（连接）：使用 + 运算符将两个字符串连接起来。
def str_concatenation():
    str1 = "Hello"
    str2 = "World"
    result = str1 + ", " + str2  # 返回 "Hello, World"
    print(result)

def str_index():
    text = "Python"
    char = text[0]  # 返回 "P"
    substring = text[2:5]  # 返回 "tho"
    print(substring)

def str_split():
    text = "apple,banana,cherry"
    fruits = text.split(",")  # 返回 ["apple", "banana", "cherry"]

def str_join():
    fruits = ["apple", "banana", "cherry"]
    text = ",".join(fruits)  # 返回 "apple,banana,cherry"

#strip()、lstrip()和rstrip()：移除字符串两侧、左侧或右侧的空格或指定字符。
def str_strip_lstrip_rstrip():
    text = "   Hello, World!   "
    stripped_text = text.strip()  # 返回 "Hello, World!"
    print(stripped_text)

#replace()：替换字符串中的特定子字符串。
def str_replace():
    text = "I love programming in Python."
    new_text = text.replace("Python", "JavaScript")  # 返回 "I love programming in JavaScript."
    print(new_text)

def str_find_index():
    text = "Hello, World!"
    position1 = text.find("World")  # 返回 7
    position2 = text.index("World")  # 返回 7
    print(position1, position2)

def str_count():
    text = "Hello, Hello, Hello, World!"
    count = text.count("Hello")  # 返回 3
    print(count)

#重复输出字符串
def str_x():
    str = "string"
    # 输出stringstring
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
    str_print()