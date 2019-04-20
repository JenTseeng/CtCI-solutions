from linkedList import SinglyLinkedList

def remove_dups(ll):
    current = ll.head
    previous = None
    vals = set()
    while current:
        if current.data not in vals:
            vals.add(current.data)
            previous = current
        else:
            previous.next = current.next
        current = current.next
        

if __name__ == '__main__':
    ll = SinglyLinkedList()
    ll.populate([1, 1, 2, 3, 4, 3, 5, 6, 5])
    print('========Before========')
    ll.printNodes()
    remove_dups(ll)
    print('========After========')
    ll.printNodes()

    ll2 = SinglyLinkedList()
    print('========Before========')
    ll2.printNodes()
    remove_dups(ll2)
    print('========After========')
    ll2.printNodes()