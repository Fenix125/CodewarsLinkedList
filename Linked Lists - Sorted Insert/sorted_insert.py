def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    while True:
        head_dt = head.data
        head_nxt = head.next
        if head_dt < data < head_nxt:
            head.next = push(data, head.next)
            new_nxt = Node(data)
            new_nxt.next = head.nxt
            node.next = new_nxt
            return node
        elif data < head_data:
            new_head = Node(data)
            new_head.next = head
            return new_head
        else:
            head.data = head_nxt
            head.nxt = head_nxt.next
