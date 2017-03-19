#Your task is to complete this function
#Function should return integer denoting the index
# indexing is done according to 0
# Left=0 and High=0
def bin_search(arr, left, high, key):

    # Base Case:
    if high >= left:

        # get middle value of the arr
        mid = left + (high - left) // 2

        report_on_search(arr, left, high, key)

        # See if they match, else keep searching
        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            return bin_search(arr, mid + 1, high, key)

        elif arr[mid] > key:
            return bin_search(arr, left, mid - 1, key)
    else:
        return -1

def test_search():
    a1 = [1, 2, 3, 4, 5, 6, 7, 8]
    a2 = [1, 3, 4, 5, 6, 7, 9]
    a3 = [1, 3, 4, 6, 7, 9]
    a4 = [1, 2, 3, 4, 4, 6, 7, 8]

    print('Result: \n\n'
        'Sample set 1: {} \n'
        'Searching for element 5...\n'
        'location: {}\n\n'.format(a1, bin_search(a1, 0, len(a1) - 1, 4)))


    print('Result: \n'
        'Sample set 2: {} \n'
        'Searching for element 5...\n'
        'location: {}\n\n'.format(a2, bin_search(a2, 0, len(a2) - 1, 4)))


    print('Result: \n\n'
        'Sample set 3: {} \n'
        'Searching for element 5...\n'
        'location: {}\n\n'.format(a3, bin_search(a3, 0, len(a3) - 1, 4)))


    print('Result: \n\n'
        'Sample set 4: {} \n'
        'Searching for element 5...\n'
        'location: {}\n\n'.format(a4, bin_search(a4, 0, len(a4) - 1, 4)))

def report_on_search(arr, low, high, key):

    # Get middle key one more time
    midkey  = low + (high - low) // 2

    # Format array to only show relevant elements
    branch  = ' '.join(['-' if (i < low or i > high) else str(j) for i,j in enumerate(arr)])
    mid     = ' '.join(['-' if i != midkey else str(j) for i, j in enumerate(arr)])
    a       = ' '.join(map(str,arr))

    print(
        'Searching...\n'
        'Array:\t{}'
        '\nBranch:\t{}'
        '\nMiddle:\t{}'
        '\nKey:\t{}\n\n'.format(a, branch, mid, key)
        )

test_search()

