def isPalindrome(head):
    
    ####################################
    #### UTIL PROGRAM
    
    def reverse(head):
        ## 3 ptr setup
        cur = head
        prev = None
            
        while cur:
            nxt = cur.next
                
            # 1. Revrese ptr
            cur.next = prev
                
            # 2. Update ptr
            prev = cur
            cur = nxt
            
            
        return prev
                
    ####################################
    #### MAIN PROGRAM  
        
    ## Edge case
    if not head.next: return True ## Single node always palindromic
        
    # 1. Find the middle
    ## Two ptr setup
    s = head
    f = s.next 
        
    while f and f.next:
        s = s.next
        f = f.next.next
        
    # 2. Reverse the sec half of LL
    ## Add the start of rev LL to the s.next
    temp = s.next
    s.next = reverse(temp)
        
    # 3. Readjust pointers
    f = s.next ## Coz slow was pointing lst to middle in even 
    s = head
        
        
    # 4. Recheck again
    while f:
        if s.val != f.val: return False
        s = s.next 
        f = f.next
        
    return True