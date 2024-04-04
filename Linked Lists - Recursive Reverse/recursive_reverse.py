class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    lst_nodes = []
    while head.next != None:
        lst_nodes.append(head.data)
        head = head.next
    lst_nodes += [head.data, None]