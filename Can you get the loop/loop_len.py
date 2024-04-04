class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def loop_size(node):
    loop_list = []
    while node.next not in loop_list:
            loop_list.append(node)
            node = node.next
    loop_list.append(node)
    return loop_list.index(node) + 1 - loop_list.index(node.next)
