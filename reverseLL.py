def solve(head):
    ## // 3 ptr setup
    prev = None
    cur = head
    
    while cur:
        nxt = cur.next 
        
        # 1. Delink 
        cur.next = prev
        
        # 2. Update Ptr 
        prev = cur
        cur = nxt
    
    return prev