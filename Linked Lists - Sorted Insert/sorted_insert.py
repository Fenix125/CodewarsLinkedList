def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    linked_lst = []
    while head.next != None:
        linked_lst.append(head.data)
        head = head.next
    linked_lst += [head.data, None]
    for ind, num in enumerate(linked_lst):
        if data > linked_lst[-2]:
            linked_lst.insert(-1, data)
            break
        if num > data:
            linked_lst.insert(ind, data)
            break
    head = None
    linked_lst.reverse()
    for i in range(1, len(linked_lst)):
        head = push(head, linked_lst[i])
    return head