import pytest
from tasks.recursion.binary_search.binary_search import binary_search

def test_find_middle_elem():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
def test_find_first_elem():
    assert binary_search([10, 20, 30, 40], 10) == 0
def test_find_last_elem():
    assert binary_search([10, 20, 30, 40], 40) == 3
def test_find_missing_elem():
    assert binary_search([1, 2, 3, 4, 5], 100) == -1
def test_find_in_empty_array():
    assert binary_search([], 5) == -1
def test_find_elem_in_1_elem_array():
    assert binary_search([7], 7) == 0
def test_find_missing_in_1_elem_array():
    assert binary_search([7], 10) == -1
def test_find_multiply_copies():
    arr = [1, 2, 2, 2, 3]
    idx = binary_search(arr, 2)
    assert idx in {1, 2, 3}
def test_large_array():
    big_arr = list(range(0, 10000))
    assert binary_search(big_arr, 9999) == 9999
    assert binary_search([-10, -5, 0, 5, 10], -5) == 1