def deleteNode(node):
    # 1. Replace the value of next node in the current
    node.val = node.next.val
        
    # 2. Delink the next node of LL 
    node.next = node.next.next
