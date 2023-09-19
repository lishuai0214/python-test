#用递归的方式实现
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


#不用递归方式实现
def quick_sort_1(arr):
    if len(arr) <= 1:
        return arr

    # 使用栈来模拟递归调用
    stack = []
    stack.append((0, len(arr) - 1))

    while stack:
        left, right = stack.pop()
        if left < right:
            pivot_index = partition(arr, left, right)
            # 将右半部分压入栈
            stack.append((pivot_index + 1, right))
            # 将左半部分压入栈
            stack.append((left, pivot_index - 1))

    return arr

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quick_sort_3(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort_3(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort_3(alist, low+1, end)

if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort_3(arr, 0, len(arr) - 1)
    print(arr)
