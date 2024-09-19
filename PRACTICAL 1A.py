import numpy as np
arr = [87, 9, 13, 120, 14, 35]
def sorting(arr):
    arr.sort()
    return arr
print(sorting(arr))
def binary_search(arr, el, start, end):
    mid = (start + end) // 2
    if el == arr[mid]:
        return mid
    if el < arr[mid]:
        return binary_search(arr, el, start, mid-1)
    else:
        return binary_search(arr, el, mid+1, end)
print(binary_search(arr, 35, 0, len(arr)))
def merge():
    a = [17, 3, 23, 45, 64, 12]
    b = [1, 33, 47]
    merged_list = np.concatenate((a, b))
    return merged_list
print(merge())
def rev():
  rev_list = np.flipud(arr)
  return rev_list
print(rev())
