def reverse(head):
    if head == None:
        return None
    lst_nodes = []
    while head.next != None:
        lst_nodes.append(head.data)
        head = head.next
    lst_nodes += [head.data]
    lst_nodes.reverse()
    lst_nodes += [None]
    lst_nodes.reverse()
    head = None
    for i in range(1, len(lst_nodes)):
        head = push(head, lst_nodes[i])
    return head