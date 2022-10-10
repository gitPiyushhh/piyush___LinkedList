class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
        
    len1 = 0
    len2 = 0
        
    cur1 = list1
    cur2 = list2
        
    ans = ListNode(-1)
    temp = ans
        
    while cur1 and cur2:
            
        # 1. List1 data small
        if cur1.val < cur2.val:
            node = ListNode(cur1.val)
            cur1 = cur1.next
            
        # 2. List2 data small
        else:
            node = ListNode(cur2.val)
            cur2 = cur2.next
            
        # 3. Globals
        temp.next = node
        temp = node
        
    ## // Remaing list1
    while cur1:
        node = ListNode(cur1.val)
        temp.next = node
        temp = node
        cur1 = cur1.next
        
    ## // Remaining list2
    while cur2:
        node = ListNode(cur2.val)
        temp.next = node
        temp = node
        cur2 = cur2.next
        
    return ans.next