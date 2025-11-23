import pytest
from tasks.data_stuctures.double_connected_node.double_connected_node import turn_list, DoubleConnectedNode

def list_to_double_connected(values):
    """
    Change list into doubly linked list
    """
    nodes = [DoubleConnectedNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    return nodes[0]


def double_connected_to_list(head):
    """
    Change doubly linked list into list
    """
    result = []
    cur = head
    while cur:
        result.append(cur.value)
        cur = cur.next
    return result


def test_one_node():
    node = DoubleConnectedNode(10)
    new_head = turn_list(node)
    assert new_head is node
    assert new_head.next is None
    assert new_head.prev is None
    
def test_two_nodes():
    head = list_to_double_connected([1, 2])
    new_head = turn_list(head)
    assert double_connected_to_list(new_head) == [2, 1]
    assert new_head.next.prev is new_head
   
def test_chars():
    head = list_to_double_connected(["a", "b", "c", "d"])
    new_head = turn_list(head)
    assert double_connected_to_list(new_head) == ["d", "c", "b", "a"]
    
    d, c, b, a = new_head, new_head.next, new_head.next.next, new_head.next.next.next
    assert d.prev is None
    assert d.next is c
    assert c.prev is d
    assert c.next is b
    assert b.prev is c
    assert b.next is a
    assert a.prev is b
    assert a.next is None
    
def test_numbers():
    head = list_to_double_connected([5, 6, 7])
    new_head = turn_list(head)
    cur = new_head
    while cur.next:
        assert cur.next.prev is cur
        cur = cur.next
       
def test_large_list():
    big_list = list(range(1000))
    head = list_to_double_connected(big_list)
    new_head = turn_list(head)
    assert double_connected_to_list(new_head) == list(reversed(big_list))
    cur = new_head
    while cur.next:
        assert cur.next.prev is cur
        cur = cur.next
