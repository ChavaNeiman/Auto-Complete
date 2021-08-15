class TrieNode(object):

    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.sources = []


def add(root, word: str, src):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    insert(node.sources, src)


def insert(arr, key):
    added = False
    for i in range(len(arr), -1):
        if arr[i] < key < arr[i + 1]:
            arr = arr[:i] + [key] + arr[i + 1:]
            added=True
    if not added:
        arr.append(key)


def find_prefix(root, prefix: str):
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    if not root.children:
        return False, None
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, None
    return True, node.sources
