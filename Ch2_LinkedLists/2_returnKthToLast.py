from linkedList import SinglyLinkedList

def return_kth_to_last_counter(ll, k):
    """ Return kth to last node, solution using LL size"""
    
    # determine length of LL
    counter = 0
    current = ll.head
    while current:
        counter += 1
        current = current.next

    if counter < k: # not enough nodes in LL
        return None
    else:
        current = ll.head
        for i in range(counter-k):
            current = current.next
        return current


def return_kth_to_last_pointers(ll, k):
    """ Return kth to last node, solution with 2 pointers """

    runner = ll.head
    follower = ll.head
    steps_ahead = 0

    while steps_ahead < k and runner:
        steps_ahead += 1
        runner = runner.next

    if steps_ahead != k: # not enough nodes in list
        return None
    else:
        while runner:
            runner = runner.next
            follower = follower.next
        return follower


def return_kth_to_last_recursion(root, k):
    """ Return kth to last node, recursive solution """

    if not root:
        return 1

    result = return_kth_to_last_recursion(root.next, k)
    if result == k:
        return root
    elif not isinstance(result, int): # node is returned from lower level
        return result
    else:
        return result+1


if __name__ == '__main__':
    
    # create test linked list
    ll = SinglyLinkedList()
    ll.populate(['a', 'b', 'c', 'd'])

    # test counter method
    node1 = return_kth_to_last_counter(ll,2)
    node2 = return_kth_to_last_counter(ll,4)
    node3 = return_kth_to_last_counter(ll,10)
    assert node1.data == 'c'
    assert node2.data == 'a'
    assert node3 == None
    
    # test pointer method
    node1 = return_kth_to_last_pointers(ll,2)
    node2 = return_kth_to_last_pointers(ll,4)
    node3 = return_kth_to_last_pointers(ll,10)
    assert node1.data == 'c'
    assert node2.data == 'a'
    assert node3 == None

    node1 = return_kth_to_last_recursion(ll.head,2)
    node2 = return_kth_to_last_recursion(ll.head,4)
    assert node1.data == 'c'
    assert node2.data == 'a'

    print("All tests passed")