from tasks.sorts.merge_sort.solution import merge_sort

def test():
    """
    Test that 'merge_sort' function sorts different arrays
    """
    print("Tests started")
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == sorted([3, 1, 4, 1, 5, 9, 2, 6])
    assert merge_sort([2, 3, 2, 1, 3]) == sorted([2, 3, 2, 1, 3])
    assert merge_sort([-1, -3, 2, 0, -2]) == sorted([-1, -3, 2, 0, -2])
    print("Tests were successful")

test()