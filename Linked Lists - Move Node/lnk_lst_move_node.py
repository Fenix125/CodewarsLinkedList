def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    if source == None:
        raise IndexError
    node_source = source.next
    new_dest = Node(source.data)
    new_dest.next = dest
    return Context(node_source, new_dest)