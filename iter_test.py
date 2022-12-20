it = iter([1, 2, 3])  # list 是可迭代对象哦
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# next(it)  # StopIretation; 普通的可迭代对象是可复用的,而迭代器是一次性的,回不了头的

it = iter("ABCD")  # string 也是可迭代对象
for i in it:
    print(i, end=" ")  # A B C D
for i in it:
    print(i, end=" ")  # ⽆输出