class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def turn_list(node: DoubleConnectedNode):
    """
    Reverses a DLL
    Args:
        node: Head of DLL
    Returns:
        node: Head of reversed DLL
    """
    back_node = node
    while back_node.next is not None:
        back_node = back_node.next
    node = back_node
    cur_node = node
    while cur_node is not None:
        temp = cur_node.next
        cur_node.next = cur_node.prev
        cur_node.prev = temp
        cur_node = cur_node.next
    return node
