def merge_sort(arr):
    if not (n := len(arr)) > 0:
        return

    while(len(arr)>2):
        pass


unsorted_list = []
unsorted_list = [int(i) for i in input("Enter the list items : ").split()]

print("\nUnsorted list is: ", unsorted_list)
print("Sorted list is: ", merge_sort(unsorted_list))
