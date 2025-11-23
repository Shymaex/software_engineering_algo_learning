def merge_sort(arr):
    """
    Sorts array with a merge sort
    Args:
        Array to sort
    Returns:
        Sorted array
    """
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    merge = []

    while left_arr and right_arr:
        if left_arr[0] <= right_arr[0]:
            merge.append(left_arr.pop(0))
        else:
            merge.append(right_arr.pop(0))
    merge.extend(left_arr or right_arr)
    return merge
