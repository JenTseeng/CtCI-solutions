from linkedList import SinglyLinkedList

def sum_lists(ll1, ll2):
    """ Sum 2 numbers represented by a linked list """

    node1 = ll1.head
    node2 = ll2.head
    carryover = 0
    output = SinglyLinkedList()

    while node1 or node2 or carryover:
        total = carryover

        if node1:
            total += node1.data
            node1 = node1.next

        if node2:
            total += node2.data
            node2 = node2.next

        digit = total%10
        carryover = total//10
        output.addNode(digit)

    return output


if __name__ == '__main__':
    ll1 = SinglyLinkedList()
    ll2 = SinglyLinkedList()
    ll1.populate([4, 8])
    ll2.populate([7, 3, 8])
    summed_list = sum_lists(ll1, ll2)
    summed_list.printNodes()

