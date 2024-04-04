def get_nth(node, index):
    if not node or index < 0:
        raise IndexError
    i = 0
    while i != index:
        node = node.next
        i += 1
    if node is None:
        raise IndexError
    return node
  