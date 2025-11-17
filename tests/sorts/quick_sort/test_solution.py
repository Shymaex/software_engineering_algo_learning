from tasks.sorts.quick_sort.solution import quick_sort

def test():
    """
    Test that 'quick_sort' function sorts different arrays
    """
    print("Tests started")
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == sorted([3, 1, 4, 1, 5, 9, 2, 6])
    assert quick_sort([2, 3, 2, 1, 3]) == sorted([2, 3, 2, 1, 3])
    assert quick_sort([-1, -3, 2, 0, -2]) == sorted([-1, -3, 2, 0, -2])
    print("Tests were successful")

test()