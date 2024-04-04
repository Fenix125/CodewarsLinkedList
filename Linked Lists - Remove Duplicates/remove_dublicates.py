class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head == None:
        return None
    if head.next == None:
        return head
    lst_nodes = []
    while head.next != None:
        lst_nodes.append(head.data)
        head = head.next
    lst_nodes += [head.data, None]
    lst_nodes = list(set(lst_nodes))
    lst_nodes.reverse()
    head = None
    for i in range(1, len(lst_nodes)):
        head = push(head, lst_nodes[i])
    return head