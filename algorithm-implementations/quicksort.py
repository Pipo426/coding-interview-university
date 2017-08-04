
def quicksort(array):
    print array
    if len(array) <= 1:
        return array
    pivot_index = len(array) - 1
    i = 0
    for element in array:
        if pivot_index == i:
            break
        if array[i] > array[pivot_index]:
            array.insert(pivot_index, array.pop(i))
            pivot_index = pivot_index - 1
        else:
            i = i + 1
    # print array
    # quicksort(array[:pivot_index])
    return [].extend(quicksort(array[:pivot_index])).append(array[pivot_index]).extend(quicksort(array[pivot_index + 1:]))

# array = [3, 7, 8, 5, 2, 1, 9, 5, 4]
array = [3, 2, 1]
print quicksort(array)
