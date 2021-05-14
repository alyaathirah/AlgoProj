class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
        self.value = int


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word, val):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

        if node.is_end:
            node.value = val

    def dfs(self, node, pre):
        if node.is_end:
            self.output.append((pre + node.char))
            #self.output.append(node.value)
            self.count.append(node.value)
        for child in node.children.values():
            self.dfs(child, pre + node.char)

    def search(self, x):
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return[]

        self.output = []
        self.count = []
        self.dfs(node, x[:-1])
        return [self.output, sum(self.count)]













