class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def trverse(head):
    currentnode=head
    while currentnode:
        print(currentnode.data,end='->')
        currentnode=currentnode.next
    print("Null")
node1=Node(1)
node2=Node(5)
node3=Node(7)

node1.next=node2
node2.next=node3

trverse(node1)