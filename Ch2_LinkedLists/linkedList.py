class SinglyLinkedListNode:
    """ Node class for singly linked list """

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """ Singly Linked List Class"""

    def __init__(self, values = None):
        self.head = None
        self.tail = None


    def addNode(self, value):
        """ method to add new node to SLL"""

        new_node = SinglyLinkedListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node


    def removeValue(self, value):
        """ method to remove node with certain value from SLL """

        current = self.head
        previous = None
        
        while current:
            if current.data == value:
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None

                elif current == self.head:
                    self.head = current.next

                elif current == self.tail:
                    self.tail = previous

                else:
                    current.data = current.next.data
                    current.next = current.next.next
                
                break

            else:
                previous = current
                current = current.next

    
    def printNodes(self):
        """ method to print all node values in SLL """

        vals = []
        current = self.head
        while current:
            vals.append(str(current.data))
            current = current.next

        print('-->'.join(vals))


    def populate(self, value_list):
        """ method to create SLL from list of values """

        for value in value_list:
            self.addNode(value)