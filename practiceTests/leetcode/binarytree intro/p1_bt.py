import json


# Amulya's Academy

#
# class Node:
#     def __init__.py(self, key):
#         self.right = None
#         self.left = None
#         self.int_data = key
#
#     # def __repr__(self):
#     #     return "Binary Tree as:\n{}\n{}\n{}".format(self.int_data, self.left, self.right)
#
#     def get_current_node(self):
#         return self.int_data
#
#     def set_left_node(self, key):
#         self.left = key
#
#     def set_right_node(self, key):
#         self.right = key
#
#     def get_left_node(self):
#         return self.left
#
#     def get_right_node(self):
#         return self.left
#

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, int_data):
        if self.key is None:
            self.key = int_data
            return
        if self.key == int_data:
            return
        if int_data < self.key:
            if self.left:
                print("{} inserted on the left of the root".format(int_data))
                self.left.insert(int_data)
            else:
                print("{} is not inserted on the left of the root".format(int_data))
                self.left = Node(int_data)
        else:
            if self.right:
                print("{} inserted on the right of the root".format(int_data))
                self.right.insert(int_data)
            else:
                print("{} is not inserted on the right of the root".format(int_data))
                self.right = Node(int_data)

    def search(self, int_data):
        if self.key == int_data:
            print("Node is found.")
            return
        if int_data < self.key:
            if self.left:
                print("performed search on left tree.")
                self.left.search(int_data)
            else:
                print("Node is not present in the tree")

        else:
            if self.right:
                print("performed search on right tree.")
                self.right.search(int_data)
            else:
                print("Node is not present in the tree")

    def preorder(self):
        print(self.key)
        if self.left:
            self.preorder()
        if self.right:
            self.preorder()


# class TUF:
#
#     def __init__.py(self, curr_node, in_order_list):
#         self.in_order_list = in_order_list
#         self.curr_node = curr_node
#         self.__in_order_trav__(self.curr_node)
#
#     def __in_order_trav__(self, curr_node):
#         if curr_node is None:
#             return
#         print(curr_node.data)
#         self.__in_order_trav__(curr_node.left)
#         self.in_order_list.append(curr_node.data)
#         self.__in_order_trav__(curr_node.right)


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    root = Node(10)
    item_list = [6, 3, 1, 6, 98, 3, 7]
    for i in item_list:
        root.insert(i)

    # tuf = TUF(root)
    # left_node = Node(2)
    # right_node = Node(3)
    # leaf_node = Node(5)
    # print(tuf.in_order_list)
    return


if __name__ == '__main__':
    print(main())
