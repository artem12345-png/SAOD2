class TreeNode:
    def __init__(self):
        self.children = list()

    def insert(self, key, value=None):
        self.key = key

        if len(self.key) == 0:
            self.value = value
            return
        letter = self.key[0]
        if letter in self.children:
            self.insert(self.key[1:], value)
        else:
            self.children.append(letter)
            self.insert(self.key[1:], value)

    # def lookup(self):


a = TreeNode()
a.insert('artem', 213)
a.insert('hjwdbchjbwdhbchjwdjchjwvcgvgvvdvwgcvtywrvurwvfyubewhjdyuwgjwjvwrjbvhjrgvbefvbyrbcb', 3746374)
print(a.children)
print(a.value)


