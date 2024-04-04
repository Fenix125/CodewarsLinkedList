class Node:
    def __init__(self, name, next=None):
        self.next = next
        self.name = name
    
def push(head, data):
    # Your code goes here.
    node = Node(data)
    node.next = head
    return node
def swap_pairs(head):
    if head == None or head.next == None:
        return head
    temp_node = swap_pairs(head.next.next)
    node_main = head.next
    head.next.next = head
    head.next = temp_node
    head = node_main
    return head


c = Node('C')
b = Node('B', c)
a = Node('A', b)
print(swap_pairs(a))