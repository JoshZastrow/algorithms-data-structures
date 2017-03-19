def qsort(arr):
    left = 0
    right = len(arr) - 1

    return _qsort(arr, left, right)


def _qsort(arr, left, right):

    if left <= right:

        pvt = partition(arr, left, right)
        _qsort(arr, left, pvt - 1)
        _qsort(arr, pvt + 1, right)

    return arr


def partition(ar, left, right):

    pivot = right
    swap_spot = left - 1

    for instance in range(left, right):

        # print_sort_status(arr, left, right, swap_spot, instance)

        if ar[instance] <= ar[pivot]:

            swap_spot += 1
            ar[instance], ar[swap_spot] = ar[swap_spot], ar[instance]

    # Swap pivot value
    swap_spot += 1
    ar[pivot], ar[swap_spot] = ar[swap_spot], ar[pivot]

    return swap_spot


def test_sort():

    a1 = [1, 5, 7, 3, 8, 2, 4, 8, 9, 10]
    print(qsort(a1))


def print_sort_status(arr, l, r, s, i):
    if arr[i] <= arr[r]:
        print(' '.join(map(str, arr)),
              '\nleft: {} ({})\nright: {} ({})\nswap spot:'
              ' {}\nindex: {}\n\n'.format(l, arr[l], r, arr[r], s, i))
    else:
        print(' '.join(map(str, arr)), ' <-- no swap'
              '\nleft: {}\nright: {}\nswap spot:'
              ' {}\nindex: {}\n\n'.format(l, r, s, i))


test_sort()