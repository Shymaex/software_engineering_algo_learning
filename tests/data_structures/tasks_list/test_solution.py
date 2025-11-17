from tasks.data_stuctures.tasks_list.solution import print_all, Node


def test():
    """
    Test that 'print_all' function print all nodes in lists
    """
    print("Tests started")
    print("A")
    node = Node("A")
    print_all(node)
    print()
    
    
    print("ABC")
    n3 = Node("C")
    n2 = Node("B", n3)
    n1 = Node("A", n2)
    print_all(n1)
    print()
    
    print("12345")
    n5 = Node(5)
    n4 = Node(4, n5)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    print_all(n1)
    print()
    
    print("0-999")
    head = None
    for i in range(999, -1, -1):
        head = Node(i, head)
    print_all(head)
    print()

    print("zyx")    
    n3 = Node("x")
    n2 = Node("y", n3)
    n1 = Node("z", n2)
    print_all(n1)
    print()
    
    print("hello, true, 42, None")
    n4 = Node(None)
    n3 = Node(42, n4)
    n2 = Node(True, n3)
    n1 = Node("hello", n2)
    print_all(n1)
    
    print("Tests ended")
    
test()