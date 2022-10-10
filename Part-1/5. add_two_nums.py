class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    #############################################
    ##### UTIL PROGRAMS
    
    def reverse(head):            
        cur = head
        prev = None
            
        ## 3 ptr setup
        while cur:
            nxt = cur.next
                
            # 1. Delink
            cur.next = prev
                
            # 2. Update ptr
            prev = cur
            cur = nxt
            
        return prev
        
    h1 = l1
    h2 = l2
    
    #############################################
    ##### MAIN PROGRAM
    
    ans = ListNode(-1)
    carry = 0
    cur = ans
        
    while h1 or h2:
        if h1 and h2:
            sm = h1.val + h2.val + carry
            h1 = h1.next
            h2 = h2.next
            
        else:
            if h1:
                sm = h1.val + carry
                h1 = h1.next
            
            if h2:
                sm = h2.val + carry
                h2 = h2.next
            
            
        carry = sm // 10 ## Update carry for next iteration
        sm = sm % 10
        temp = ListNode(sm)
        cur.next = temp
        cur = cur.next
        
    if not h1 and not h2 and carry:
        temp = ListNode(carry)
        cur.next = temp
        
    print(ans.next.val)
        
    return ans.next