class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        result = list()
        if self.head is None:
            return result

        node = self.head
        while node:
            result.append(node.data)
            node = node.next

        return result

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

    def insert_beginning(self, data):
        # TC = O(1)
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
            return

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        # TC = O(1)
        if self.head is None:
            self.insert_beginning(data)
            return
        # if self.last_node is None:
        #     current = self.head
        #     while current.next is not None:
        #         current = current.next
        #
        #     current.next = Node(data)
        #     self.last_node = current.next
        #
        # else:
        #     self.last_node.next = Node(data)
        #     self.last_node = self.last_node.next
        self.last_node.next = Node(data)
        self.last_node = self.last_node.next

    def get_user_by_id(self, user_id):
        current = self.head

        while current:
            if current.data['id'] == user_id:
                return current.data

            current = current.next

        return None



ll = LinkedList()
ll.insert_beginning("data")
ll.insert_beginning("data1")
ll.insert_beginning("data2")
ll.insert_at_end("data3")
ll.insert_at_end("data4")
ll.insert_at_end("data5")
ll.print_linked_list()