def selectionSort(array):
    for i in range(len(array)):
        min_index = min(range(i, len(array)), key=array.__getitem__)
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Do not change the following code
data = list(map(int, input().split(', ')))
print(selectionSort(data))
