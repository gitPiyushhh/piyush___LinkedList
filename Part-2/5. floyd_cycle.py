def detectCycle(head):
    ## // Edge case {if no elem is present}
    if not head or not head.next:
        return None
        
    ## // speed ptr setup
    s = head
    f = head
        
    # 1. Find that cycle exist or not   
    while f and f.next:
        s = s.next
        f = f.next.next
            
        if s == f: break
        
    if not f or not f.next: return None ## // No cycle here
        
        
    # 2. Reset ptr
    f = head
        
    # 3. Floyd cycle detection algo implement
    while s != f:
        f = f.next
        s = s.next
        
    return s