def quick_sort(arr):
    """
    Sorts array with a quick sort
    Args:
        Array to sort
    Returns:
        Sorted array
    """
    if not arr:
        return arr
    pivot = arr.pop()
    left_arr = []
    right_arr = []
    for num in arr:
        if num < pivot:
            left_arr.append(num)
        else:
            right_arr.append(num)
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)