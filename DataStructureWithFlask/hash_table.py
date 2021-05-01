class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None]* table_size

    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            # This module operation guarantees that the hash table size will not exceed given size
            hash_value = (hash_value * ord(i)) % self.table_size

        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)

        # if element is already present at that hash value in the hash table. This result in collision
        else:
            node = self.hash_table[hashed_key]
            while node.next:
                node = node.next

            node.next = Node(Data(key, value), None)

    def get_value(self, key):
        """
        Get value from the hash table based on the key provided in the input
        """
        hashed_key = self.custom_hash(key)

        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]

            if node.next is None:
                return node.data.value

            while node.next:
                if key == node.data.key:
                    return node.data.value

                node = node.next

            if node.data.key == key:
                return node.data.value

        return None

    def print_table(self):
        print("{")

        for index, value in enumerate(self.hash_table):
            if value is not None:
                llist_string = ""
                node = value

                if node.next:
                    while node.next:
                        llist_string += (
                                str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )

                        node = node.next

                    llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )

                else:
                    print(f"[{index}] {value.data.key} : {value.data.value}")

            else:
                print(f"[{index}] {value}")

        print("}")
