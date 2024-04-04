def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    while True:
        head_dt = head.data
        head_nxt = head.next
        if head_dt < data < head_nxt:
            node = Node(head_dt)
            new_nxt = Node(data)
            new_nxt.next = head.nxt
            node.next = new_nxt
            return node
        else:
            head.data = head_nxt
            head.nxt = head_nxt.next
