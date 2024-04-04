def push(head, data):
    # Your code goes here.
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    main_node = (push(push(push(None, 3), 2), 1))
    return main_node