from tasks.recursion.binary_search.solution import binary_search

def test():
    """
    Test that 'binary_search' function works as binary search
    """
    print("Tests started")
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([10, 20, 30, 40], 10) == 0
    assert binary_search([10, 20, 30, 40], 40) == 3
    assert binary_search([1, 2, 3, 4, 5], 100) == -1
    assert binary_search([], 5) == -1
    assert binary_search([7], 7) == 0
    assert binary_search([7], 10) == -1
    arr = [1, 2, 2, 2, 3]
    idx = binary_search(arr, 2)
    assert idx in {1, 2, 3}
    big_arr = list(range(0, 10000))
    assert binary_search(big_arr, 9999) == 9999
    assert binary_search([-10, -5, 0, 5, 10], -5) == 1
    print("Tests were successful!")
    
test()