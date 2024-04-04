def stringify(node):
    if not node:
        return 'None'
    stringa = ''
    while node.next is not None:
        stringa += str(node.data) + ' -> '
        node = node.next
    stringa += str(node.data) + ' -> ' + 'None'
    return stringa