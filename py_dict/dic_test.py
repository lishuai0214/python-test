def dic_base():
    dict = {'Tom': 93, 'Jim': 80, 'Lily': 100}
    print(dict)
    print(dict['Tom'])
    print(dict.get('Tom'))
    print(dict.get('Lison', 0))

def dic_keys():
    dict = {'Tom': 93, 'Jim': 80, 'Lily': 100}
    print(dict.keys()) #该方法返回一个视图对象dict_keys
    #print(dict.keys()[0]) # keys方法返回的对象不支持索引,报错
    print(list(dict.keys()))
    print(list(dict.values()))
    print(list(dict.items()))

def dic_delete():
    dict = {'Tom': 93, 'Jim': 80, 'Lily': 100}
    print(dict)
    del dict['Tom']
    print(dict)

def dic_clear():
    dict = {'Tom': 93, 'Jim': 80, 'Lily': 100}
    print(dict)
    dict.clear()
    print(dict)

def dic_value_in_dic():
    dict = {'Tom': 93, 'Jim': 80, 'Lily': 100}
    print(93 in dict.values())
    print(43 in dict.values())

def dic_key_in_dic():
    dict = {'Tom': 93, 'Jim': 80, 'Lily': 100}
    print('Tom' in dict)
    print('Jerry' in dict)

def dic_for():
    dict = {'Tom': 93, 'Jim': 80, 'Lily': 100}
    for key, value in dict.items():
        print(key, value)

if __name__ == '__main__':
    dic_base()
    dic_keys()
    dic_delete()
    dic_clear()
    dic_value_in_dic()
    dic_key_in_dic()
    dic_for()

