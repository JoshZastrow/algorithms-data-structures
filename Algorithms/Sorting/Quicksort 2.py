def qsort(arr):
    low = 0
    high = len(arr) - 1
    return _sort(arr, low, high)


def _sort(arr, low, high):

    # Run the partition and sort while the low index
    # is less than the high index
    if low < high:

        # partition array around a pivot
        # return the pivot location
        pvt = partition(arr, low, high)

        # sort the lower and upper partitions
        _sort(arr, low, pvt - 1)
        _sort(arr, pvt + 1, high)

    return arr

def partition(arr, low, high):

    # Select a pivot value
    pvt = arr[high]

    # Partition each value around pivot
    # Swap smaller values to the left
    wall = low - 1

    for spt in range(low, high):

        # Compare element with pvt
        # Increment wall spot and swap
        if arr[spt] <= pvt:
            wall += 1
            arr[spt], arr[wall] = arr[wall], arr[spt]


    # Swap pivot with next wall spot
    # Return the pivot
    wall += 1
    arr[high], arr[wall] = arr[wall], arr[high]

    return wall


a = [3, 5, 7, 1, 2, 5, 9, 4]
print(a)
print(qsort(a))

