import copy
class Node:
    def __init__(self, next=None):
        self.next = next
    
def push(head, data):
    # Your code goes here.
    node = Node(data)
    node.next = head
    return node

def swap_pairs(head):
    if head == None or head.next == None:
        return head
    head_next = head.next
    head_next.next = head
    return head


c = Node()
b = Node(c)
a = Node(b)

print(swap_pairs(a))