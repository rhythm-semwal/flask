class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_linked_list(self):
        if self.head is None:
            print("None")

        node = self.head
        ll_string = ""

        while node:
            ll_string += f"{str(node.data)} ->"
            node = node.next

        ll_string += "None"

        print(ll_string)


ll = LinkedList()
node4 = Node("data4", None)
node3 = Node("data3", node4)
node2 = Node("data2", node3)
node1 = Node("data1", node2)

ll.head = node1
ll.print_linked_list()