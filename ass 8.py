list1 = [2,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,8,9]
target = int(input('Enter a number: '))
low = 0
high = len(list1) - 1
first = -1

while low <= high:
    mid = (low + high) // 2

    if target == list1[mid]:
        first = mid
        high = mid - 1   # keep searching left for first occurrence

    elif target > list1[mid]:
        low = mid + 1

    else:
        high = mid - 1

if first != -1:
    print(f'The first occurrence of the target is at index {first}')
else:
    print('Element not found')
