def removeNthFromEnd(head, n):
    # Speed pointers setup
    s = head
    f = head
    temp = head
        
    # 1. Make fast ptr ahead
    for i in range(n):
        f = f.next
        
        
    if n >= 2:
        for i in range(2):
            temp = temp.next
        
    ## Edge case when we have node to remove more than large
    if f is None:
        return head.next
        
    # 2. Move ptr till less than target
    while f and f.next:
        s = s.next
        f = f.next
        temp = temp.next
       
    # 3. Remove node {if last node needs to be del then make last sec point to None}
    if n == 1: s.next = f.next
    else: s.next = temp
        
    return head