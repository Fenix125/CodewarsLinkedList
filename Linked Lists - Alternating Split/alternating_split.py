def push(head, data):
    node = Node(data)
    node.next = head
    return node

def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    if head == None or head.next == None:
        raise ValueError
    lst_split = []
    while head.next != None:
        lst_split.append(head.data)
        head = head.next
    lst_split += [head.data]
    list_first = []
    list_second = []
    for i in range(1, len(lst_split), 2):
        list_first.append(lst_split[i])
        list_second.append(lst_split[i + 1])
    list_first.reverse()
    list_second.reverse()
    head1 = None
    for i in range(1, len(list_first)):
        head1 = push(head, list_first[i])
    head2 = None
    for i in range(1, len(list_second)):
        head2 = push(head, list_second[i])
    return Context(head1, head2)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
d.next = e
c.next = d
b.next = c
a.next = b
print(alternating_split(a))