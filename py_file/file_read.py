def file_read_1():
    # 打开一个文件
    fr = open("foo.txt", "r")

    print(fr.name)

    # 2.读取文件中的数据
    print(fr.read(3))    # 得到 abc 读的是字符
    print(fr.read(4))    # 得到 defg 读的是字符
    print(fr.read())      # 得到 1234567(读取剩余的所有)

    # tell()：返回已读的字节数
    print(fr.tell())        #接上面的代码的到 14

    # seek(num)：将文件描述符移动到num字节位,返回新的文件位置,从num字节位开始
    fr.seek(4)         # 表示起始位置从第四位后面的开始
    print(fr.read())   #得到efg1234567

    # 3.关闭文件
    fr.close()

def file_read_2():
    for line in open('foo.txt', 'r'):
        print(line, end='')

if __name__ == '__main__':
    file_read_2()