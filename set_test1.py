def set_test1():
    s = {1,2,3,4,5,}
    s.add('5')
    print(s)

def set_test2():
    # update(x),将x添加到集合中，且参数可以是列表、元组、字典等
    s = set(('a', 'cc', 'f'))
    # 添加字典只能添加不可变的--键
    dict_1 = {'name': 'bb', 'age': 'cc', 'f': 11}
    s.update(dict_1)
    print("添加字典" + str(s))

def set_test3():
    s = set(('a', 'cc', 'f'))
    tup_1 = (1, 2,)
    s.update(tup_1)
    print(s)

def set_remove1():
    # 移除集合中元素，如果移除的元素不在集合中将发生错误
    s = set(('a', 'cc', 'f'))
    s.remove('cc')
    print(s)
    s.remove('c666c')
    print(s)

def set_discard1():
    # 移除集合中元素，如果移除的元素不在集合中不会发生错误
    s = set(('a', 'cc', 'f'))
    s.discard('mm')
    print(s)

def set_clear1():
    # 清空集合
    s = set(('a', 'cc', 'f'))
    s.clear()
    print(s)

def set_difference1():
    # difference求差集 或者用 -
    s = set(('a', 'cc', 'f'))
    s1 = {'a', 'f', 1, 'ww'}
    # 两种求差集的方法
    print("在s中不在s1中: " + str(s.difference(s1)))
    print('在s1中不在s中： ' + str(s1 - s))

def set_intersection1():
    s = set(('a', 'cc', 'f'))
    s1 = {'a', 'f', 1, 'ww'}
    # 同时在集合s 和 s1 中的元素
    print(s.intersection(s1))
    print(s1 & s)

def set_union1():
    s = set(('a', 'cc', 'f'))
    s1 = {'a', 'f', 1, 'ww'}
    # 元素在集合 s 中或在集合 s1 中
    print(s.union(s1))
    print(s1 | s)

def sysmmetric_difference1():
    s = set(('a', 'cc', 'f'))
    s1 = {'a', 'f', 1, 'ww'}
    # 除集合s和集合s1共有的以外的元素
    print(s.symmetric_difference(s1))
    print(s1 ^ s)


if __name__ == '__main__':
    set_intersection1()