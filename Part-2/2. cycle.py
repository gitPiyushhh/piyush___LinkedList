def hasCycle(head):
    # // 2 ptr setup
    s = head
    f = head
        
    # // f.next coz we r tryin to access f.next.next and next of None is not possible
    while f and f.next:
        s = s.next
        f = f.next.next
            
        if s == f: return True
            
    return False