def print_hi():
    names = [4, 8, 9, 9, 0, 6, 67, 100, 56, 30]
    bubleSort(names)
    print(names)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubleSort(arr):
    arr_len = len(arr)
    for j in range(1, arr_len):
        for k in range(j, arr_len)[::-1]:
            if arr[k] < arr[k - 1]:
                swap(arr, k, k - 1)

if __name__ == '__main__':
    print_hi()
