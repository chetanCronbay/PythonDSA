class node():
    def __init__(self,data): #make a node
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def addNextNode(self,data): #adds node to right side ([][]->[][])
        new_node = node(data)

        if not self.head:
            self.head = new_node #if head is empty make new node as head
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current #connect new node to previous node

    def addPrevNode(self,data): #adds node to left side ([][]<-[][])
        new_node = node(data)

        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head #connects new node to head
        self.head.prev = new_node #connect head to new node
        self.head = new_node #make new node as the head

    def display(self):
        current = self.head
        
        while current:
            print(f'{current.data} <->', end=" ")
            current = current.next
        print("empty")
            


dll = DoublyLinkedList()
dll.addNextNode(10)
dll.addNextNode(20)
dll.addPrevNode(30)
dll.display()