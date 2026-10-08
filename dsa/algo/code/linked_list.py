
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def iterate_linked_list(head):
    if head is None:
        return
    p = head
    while p is not None:
        print(p.data, end=" ")
        p = p.next
    print()

def find_last_node(head):
    if head is None:
        return None
    p = head
    while p.next is not None:
        p = p.next
    return p

def find_second_last_node(head):
    if head is None:
        return None
    if head.next is None:
        return None
    p = q = head
    while p.next is not None:
        q = p
        p = p.next
    return q

def find_kth_from_end(head, k):
    if head is None:
        return None
    p = head

    while k != 1 and p.next is not None:
        p = p.next
        k -= 1
    
    if p.next is None and k != 1:
        return None
    
    q = head
    while p.next is not None:
        p = p.next
        q = q.next

    return q

def make_last_node_first(head):
    if head is None:
        return None
    if head.next is None:
        return head

    p = q = head
    while p.next is not None:
        q = p
        p = p.next

    p.next = head
    q.next = None
    head = p
    return head

def reverse_linked_list(head):
    if head is None:
        return None
    if head.next is None:
        return head

    p = head
    q = r = None

    while p is not None:
        r = q
        q = p
        p = p.next
        q.next = r

    head = q
    return head

def find_middle(head):
    if head is None:
        return None
    p = q = head

    while q is not None and q.next is not None:
        q = q.next.next
        p = p.next

    return p

def insert_at_beginning(head, x):
    p = Node(x)
    p.next = head
    head = p
    return head

def insert_at_end(head, x):
    p = Node(x)
    if head is None:
        head = p
        return head
    
    q = head
    while q.next is not None:
        q = q.next

    q.next = p
    return head

def insert_before_y(head, y, x):
    if head is None:
        return None
    
    new_node = Node(x)
    p = head
    q = None

    while p.next is not None and p.data != y:
        q = p
        p = p.next

    if p.data != y:
        return head

    q.next = new_node
    new_node.next = p
    return head

def delete_from_end(head):
    if head is None:
        return None
    p = head
    q = None

    while p.next is not None:
        q = p
        p = p.next

    q.next = None
    del p
    return head

def delete_x(head, x):
    if head is None:
        return None
    p = head
    q = None

    while p.next is not None and p.data != x:
        q = p
        p = p.next

    if p.data != x:
        return head

    q.next = p.next
    del p
    return head

def main():
    head = Node(0)
    a = Node(10)
    b = Node(20)

    head.next = a
    a.next = b

    print("list: ", end="")
    iterate_linked_list(head)

    head = insert_at_beginning(head, 5)
    print("list: ", end="")
    iterate_linked_list(head)

if __name__ == "__main__":
    main()

# output:
"""
list: 0 10 20
list: 5 0 10 20
"""