def binary_search(arr, target):
    """
    Use binary search to find target in list
    Args:
        arr - sorted array
        target - element to search
    Returns:
        index of the found element or -1 if else
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
