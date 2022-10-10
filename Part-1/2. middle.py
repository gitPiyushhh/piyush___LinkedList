def solve(head):
    # // Speed ptr setup
    s = head
    f = head
        
    while f and f.next: ## Here condn f is for even size ll, f.next is for even size ll
        f = f.next.next
        s = s.next
        
    return s