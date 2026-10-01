class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = int(input("Enter the inputs for l1"))
n2 = int(input("Enter the inputs for l2"))

head1 = None 
head2 = None 
temp = None 

def createlist(n):
    head = temp = None
    for i in range(n):
        data = int(input("enter the data for "))
        new = Node(data)
        if head is None:
            head = new
            temp = new
        else:
            temp.next = new
            temp = new
    return head

def printlist(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def mergelist(l1,l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next

head1 = createlist(n1)
head2 = createlist(n2)
print("List 1")
printlist(head1)
print("List 2")
printlist(head2)
head3 = mergelist(head1,head2)
print("Merged list")
printlist(head3)

