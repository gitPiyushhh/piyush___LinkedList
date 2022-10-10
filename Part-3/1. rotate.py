def rotateRight(head, k):
    ## Edge cases
    if not head or not head.next: return head
        
    ## Speed ptr setup
    s = head
    f = head
    cur = head
    cnt = 0
        
    # 1. Calc the len(LL)
    while cur:
        cnt += 1
        cur = cur.next
        
    rng = k % cnt
        
    ## Check for another edge case if there is same num of repeat
    if rng == 0: return head
        
    # 2. Take both speed ptr to correct pos
    for i in range(rng):
        f = f.next
            
    while f.next:
        s = s.next
        f = f.next
        
    # 3. Main processing
    temp = s.next
    s.next = None
        
    f.next = head
    head = temp
        
        
    return head