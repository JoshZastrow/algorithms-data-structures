def qsort(arr):

    # Initialize the left
    # and right side of the array
    left = 0
    right = len(arr) - 1

    # Run a private helper function
    return _qsort(arr, left, right)


def _qsort(arr, left, right):

    # base case: left side is lower than right
    if left < right:

        # Partition returns the placement of the pivot.
        # Placement of pivot splits the array into
        # higher and lower
        pivot = partition(arr, left, right)

        _qsort(arr, left, pivot - 1)
        _qsort(arr, pivot + 1, left)

    return arr


def partition(arr, left, right):

    # Pick a pivot
    pivot = right

    # initialize the swap location
    swap_spot = left - 1

    if left < right:

        # run through each element, compare to pivot
        for instance in range(left, right):

            if arr[instance] <= arr[pivot]:

                # move up the swap spot
                # switch it out with the found small elemnt
                swap_spot += 1
                arr[swap_spot], arr[instance] = arr[instance], arr[swap_spot]

        # All the spots have been compared
        # and swapped, final step is swap the pivot
        swap_spot += 1
        arr[swap_spot], arr[instance]

    return swap_spot
