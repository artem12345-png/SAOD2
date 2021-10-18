class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.children = list()



class Tree:
    def __init__(self):
        self.root = Node(' ')

    def insert(self, key, parent=None, value=None):

        if key:
            return

        elif len(key) == 1:
            new_node = Node(key, value)
            parent.children.append(new_node)
            print(parent.children.append(new_node))
            return
        # letter = key[0]
        # if letter in parent.children:
        #     new_node = Node(key, value)
        #     node.insert(self.key[1:], value)
        # else:
        #     self.children.append(letter)
        #     print(self.children)
        #     print("---" * 100)
        #     node = Node()
        #     node.insert(self.key[1:], value)

    # def lookup(self, key):
    #     if len(key) == 1:
    #         return self.value
    #     else:
    #         letter = self.key[0]






a = Tree()
a.insert('a', 213)
a.insert('hjwdbchjbwdhbchjwdjchjwvcgvgvvdvwgcvtywrvurwvfyubewhjdyuwgjwjvwrjbvhjrgvbefvbyrbcb8888888888888888', 3746374)
# print(a.lookup('a'))


