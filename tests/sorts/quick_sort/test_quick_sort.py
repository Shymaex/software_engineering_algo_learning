import pytest
from tasks.sorts.quick_sort.quick_sort import quick_sort

def test_sort_empty():
    assert quick_sort([]) == []
def test_sort_single():
    assert quick_sort([1]) == [1]
def test_sort_order():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
def test_sort_reverse_order():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
def test_sort_numbers():
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == sorted([3, 1, 4, 1, 5, 9, 2, 6])
def test_sort_with_coppies():
    assert quick_sort([2, 3, 2, 1, 3]) == sorted([2, 3, 2, 1, 3])
def test_sort_negative():
    assert quick_sort([-1, -3, 2, 0, -2]) == sorted([-1, -3, 2, 0, -2])