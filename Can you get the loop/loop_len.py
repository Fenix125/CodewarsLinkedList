class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def loop_size(node):
    loop_list = {}
    counter = 0
    while node.next not in loop_list:
        loop_list[node] = counter
        node = node.next
        counter += 1
    loop_list[node] = counter
    return loop_list[node] - loop_list[node.next] + 1


node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node3

nodes = [Node(str(_)) for _ in range(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
print(loop_size(node1))