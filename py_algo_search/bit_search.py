def binary_search(arr, low, high, x):
    # 检查基本情况
    if high >= low:
        mid = (high + low) // 2
        # 如果 mid 是 x
        if arr[mid] == x:
            return mid
        # 如果 x 大于 mid，必定在右半部分
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        # 否则在左半部分
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        # 元素不存在于数组中
        return -1

# 测试数组
arr = [2, 3, 4, 10, 40]
x = 10

# 函数调用
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("元素在数组中的索引为", str(result))
else:
    print("元素不在数组中")
