class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def loop_size(node):
    loop_list = {}
    counter = 0
    while node.next not in loop_list:
            loop_list[node] = counter
            node = node.next
            counter += 1
    return counter - loop_list[node.next]