def linked_list_from_string(s):
    s = s.strip().split(' -> ')
    i = 0
    def node_recurs(i):
        if s[i] == 'None':
            return None
        return Node(int(s[i]), node_recurs(i + 1))
    return node_recurs(i)