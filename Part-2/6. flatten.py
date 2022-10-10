class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

#########################
#### UTIL PROGRAM

def mergeTwoSorted(l1, l2):
        
    # 1. Create dumy node
    dummy = Node(-1)
    temp = dummy
        
    # 2. If both are preset
    while l1 and l2:
        # a. l1 less
        if l1.data < l2.data:
            temp.bottom = Node(l1.data)
            l1 = l1.bottom
            
        # b. l2 less
        else: 
            temp.bottom = l2 
            l2 = l2.bottom
            
        # c. Globals
        temp = temp.bottom
        
    # 3. Only l1 remaining
    if l1:
        temp.bottom = l1
        
    # 4. Only l2 remaining
    if l2:
        temp.bottom = l2
        
    return dummy.bottom
       
       
#########################
#### MAIN PROGRAM

def flatten(root):
        
    ## // Base case
    if not root or not root.next:
        return root
        
    # 1. Recurence call
    root.next = flatten(root.next)
         
    # 2. Merge
    root = mergeTwoSorted(root, root.next)
         
    return root
