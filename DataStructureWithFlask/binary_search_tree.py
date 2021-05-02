class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)

        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return

    def search(self, blog_post_id):
        if self.root is None:
            return False

        return self._search_recursive(blog_post_id, self.root)

    def _search_recursive(self, blog_post_id, node):
        if node.left is None and node.right is None:
            return False

        if blog_post_id == node.data["id"]:
            return node.data

        if blog_post_id < node.data["id"]:
            if blog_post_id == node.left.data["id"]:
                return node.left.data
            else:
                return self._search_recursive(blog_post_id, node.left)

        else:
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            else:
                return self._search_recursive(blog_post_id, node.right)
