class TriesNode():
    def __init__(self, letter):
        self.letter = letter
        self.children = []
        self.lastLeaf = False #true for the last leaf

    def addChild(self, TrieNode):
        self.children.append(TrieNode)

class Tries():
    def __init__(self): #constructor
        self.root = TriesNode(None)

    def insert(self, key):
        currentLetter = self.root
        length = len(key)

        for i in range(length):
            found = False
            for j in range(len(currentLetter.children)):
                if (currentLetter.children[j].letter == key[i]):  # check if the node has same child as key
                    nextLetter = currentLetter.children[j]
                    found = True
                    break

            if not found:
                nextLetter = TriesNode(key[i])
                currentLetter.addChild(nextLetter)
            currentLetter = nextLetter

        currentLetter.lastLeaf = True

    def search(self, text):
        currentLetter = self.root
        num=0
        for i in range(len(text)):
            num=i
            for j in range(len(currentLetter.children)):
                if (text[i] == currentLetter.children[j].letter):
                    currentLetter = currentLetter.children[j] #replace with child
                    #print(currentLetter.letter, end="")
                    break
                if (j == len(currentLetter.children)-1): #reach the end already
                    return False
            if currentLetter.lastLeaf == True and (num == len(text)-1): #reach end and last leaf == true
                return True

        return False #Word does not exist


