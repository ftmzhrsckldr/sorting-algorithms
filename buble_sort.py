def bubble_sort(arr):
    n = len(arr) - 1

    for i in range(n):
        for j in range(n - i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


unsorted_list = []
unsorted_list = [int(i) for i in input("Enter the list items : ").split()]

print(bubble_sort(unsorted_list))
