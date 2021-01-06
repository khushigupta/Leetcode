class Node:
    val = ''
    children = {}

    def __init__(self, val):
        self.val = val
        self.children = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')
        self.eow = '\n'

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # if len(word) < 1:
        #     return

        temp = self.root
        for i in range(len(word)):
            letter = word[i]
            if letter in temp.children:
                temp = temp.children[letter]
            else:
                new_node = Node(letter)
                temp.children[letter] = new_node
                temp = temp.children[letter]

        new_node = Node(self.eow)
        temp.children[self.eow] = new_node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # if len(word) == 0:
        #     return False

        temp = self.root
        new_word = list(word) + [self.eow]
        for w in new_word:
            if w not in temp.children:
                return False
            else:
                temp = temp.children[w]

        if len(temp.children) == 0:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        temp = self.root
        for p in prefix:
            if p not in temp.children:
                return False
            else:
                temp = temp.children[p]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)