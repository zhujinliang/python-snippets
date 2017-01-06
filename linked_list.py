# -*- encoding:utf8 -*-


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

def reverse_list(list_node):
    if list_node is None or list_node.next is None:
        return list_node
    head = list_node
    pre = None
    cur = list_node
    while cur:
        head = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    return head


if __name__ == '__main__':
    p = Node(0, None)
    p1 = Node(1, None)
    p2 = Node(2, None)
    p.next = p1
    p1.next = p2


    h = reverse_list(p)
    while h:
        print h.data
        h = h.next
