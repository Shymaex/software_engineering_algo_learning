class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

def print_all(node: Node):
    """
    Print all nodes in SLL
    Args:
        node: head of the SLL
    Returns:
        None
    """
    while node is not None:
        print(node.value)
        node = node.next_item