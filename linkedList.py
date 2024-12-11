# make a node class ([data][next])
class node():
    def __init__(self,data):
        self.data = data
        self.next = None

# linked list which will use nodes to connect ([head][ref]->[][]->[][])
class LinkedList():
    def __init__(self):
        self.head = None

    def addNode(self, data): #adds node at the begning
        new_node = node(data) #new empty node is made ([][])
        new_node.next = self.head #refrence is made ([][head])
        self.head = new_node #head now points to the new_node ([][head]->[new_node][])

    def appendNode(self,data): #adds node one after another
        new_node = node(data) #create a new node

        if not self.head:
            self.head = new_node #if the head is empty set new node as head
            return

        current = self.head #set current as head (current is like a pointer which points to the nodes in the list)
        
        while current.next: #traverse to the last node 
            current = current.next 
        
        current.next = new_node #point next pointer to the last node([][cur.next]->[new_node][]) after traversing to the last node it points to the new node

    def delete(self,key):
        current = self.head #setting current as head

        if current and current.data == key: #if delete node is at the begning
            self.head = current.next #set the head to point to the next node on the list
            current = None #and set the current node to null
            return
        
        prev = None #setting previous node to keep track of previous in the starting previous node is none (prev -> [head][next]->[][])

        while current and current.data != key: #traverse through the list till we find the key
            prev = current # making the previous node as the currrent
            current = current.next #makking the current as the next node
            
        if not current: #key is not eqal to any node
            return
        
        prev.next = current.next
        current = None

    def begningDel(self): #deleting at the begning
        current = self.head #setting current as head
        self.head = current.next #setting head as the next node
        current = None
        return
    
    def display(self):
        current = self.head
        while current:
            print(f'{current.data} ->', end=" ")  # Print the node's data
            current = current.next
        print('empty list')  # Indicate the end of the list

ll = LinkedList()
ll.addNode(10)
ll.addNode(20)
ll.display()
ll.begningDel()
ll.display()
ll.appendNode(30)
ll.appendNode(40)
ll.appendNode(50)
ll.appendNode(60)
ll.appendNode(70)
ll.appendNode(80)
ll.display()
ll.delete(50)
ll.display()
