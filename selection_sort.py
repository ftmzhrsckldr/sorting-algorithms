def selection_sort(unsorted):

    for i in range(len(unsorted) - 1):
        curr_min = i

        for j in range(i + 1, len(unsorted)):
            if (unsorted[j] < unsorted[curr_min]):
                curr_min = j

        unsorted[i], unsorted[curr_min] = unsorted[curr_min], unsorted[i]

    return unsorted


print(selection_sort(unsorted))
