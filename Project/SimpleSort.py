def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                #arr[j], arr[j + 1] = arr[j + 1], arr[j]      #swapping 2 elements in the list
                arr[j:j+2] = reversed(arr[j:j+2])              #swapping 2 elements in the list
            j += 1
    return arr


print(simpleSort([1, 7, 2, 8, 4, 9]))
