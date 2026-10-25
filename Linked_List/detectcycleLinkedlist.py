class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def hascycle(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False


node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)


node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node2

# traverasal
def traverse(head):
    go=head
    while go:
        print(go.data,end='->')
        go=go.next
    print("Null")

# traverse(node1)
print(hascycle(node1))

