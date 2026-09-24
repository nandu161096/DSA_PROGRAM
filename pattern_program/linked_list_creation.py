class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input("Enter the number of nodes"))

head_node = None 
tail_node = None 

for i in range(n):
    data = int(input("Enter the data"))
    new_node = Node(data)
    
    if head_node is None:
        head_node = new_node
        tail_node = new_node
    else:
        tail_node.next = new_node
        tail_node = new_node
    

curr = head_node
while curr:
    print(curr.data)
    curr = curr.next
    
