def linear_search(lst, element):
    for i in lst:
        if i == element:
            return lst.index(i)
    return -1

def binary_search(lst, element, start, end):
    mid = (start + end) // 2
    if element == lst[mid]:
        return mid
    if element < lst[mid]:
        return binary_search(lst, element, start, mid-1)
    else:
        return binary_search(lst, element, mid+1, end)

lst = [1,2,3,4,5,6,7,8,9]
element = 8
print("Select the method you want to use:")
print("1. Linear search")
print("2. Binary search")
option = int(input("Enter the option"))

if option == 1:
    print(linear_search(lst, element))
elif option == 2:
    print(binary_search(lst, element, 0, len(lst)))
