import pytest
from tasks.data_stuctures.tasks_list.tasks_list import print_all, Node


def test_single_char(capsys):
    node = Node("A")
    print_all(node)
    captured = capsys.readouterr()
    assert captured.out.strip() == "A"
    
def test_chars(capsys):
    n3 = Node("C")
    n2 = Node("B", n3)
    n1 = Node("A", n2)
    print_all(n1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "A\nB\nC"
        
def test_numbers(capsys):
    n5 = Node(5)
    n4 = Node(4, n5)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    print_all(n1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1\n2\n3\n4\n5"
    
def test_thousand_numbers(capsys):
    """
    Test that 'print_all' function can print large arrays
    """
    head = None
    for i in range(999, -1, -1):
        head = Node(i, head)
    print_all(head)
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    assert lines[0] == "0"
    assert lines[-1] == "999"
    assert len(lines) == 1000
              
def test_different_types(capsys):
    """
    Test that 'print_all' function support different types of data
    """
    n4 = Node(None)
    n3 = Node(42, n4)
    n2 = Node(True, n3)
    n1 = Node("hello", n2)
    print_all(n1)
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello\nTrue\n42\nNone"
    