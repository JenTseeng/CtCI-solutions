from linkedList import SinglyLinkedList, SinglyLinkedListNode

def partition_SLL(sll, value):
    """ Partition LL around value """

    current = sll.head
    lesserLL = SinglyLinkedList()
    greaterLL = SinglyLinkedList()

    while current:
        if current.data < value:
            lesserLL.addNode(current.data)
        else:
            greaterLL.addNode(current.data)
        current = current.next
    lesserLL.tail.next = greaterLL.head
    return lesserLL


if __name__ == '__main__':
    ll = SinglyLinkedList()
    ll.populate([1, 3, 4, 7, 2, 4, 9, 0])
    ll.printNodes()
    sortedll = partition_SLL(ll, 4)
    sortedll.printNodes()