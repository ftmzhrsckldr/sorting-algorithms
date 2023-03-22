def insertion_sort(arr):
    if not (n := len(arr)) > 0:
        return

    for i in range(1, n):
        j = i

        while (j != 0 and arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


unsorted_list = []
unsorted_list = [int(i) for i in input("Enter the list items : ").split()]

print("\nUnsorted list is: ", unsorted_list)
print("Sorted list is: ", insertion_sort(unsorted_list))
