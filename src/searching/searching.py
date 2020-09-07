def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr) ):
        if arr[i] is target:
            return i 
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle_index = start + (end - end) // 2
        middle_value = arr[middle_index]

        if middle_value is target:
            return middle_index

        elif target < middle_value:
            end = middle_index - 1

        else:
            start = middle_index + 1
    return -1  # not found


