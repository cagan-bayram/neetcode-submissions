class PrefixTree:

    def __init__(self):
        self.root = []

    def insert(self, word: str) -> None:
        self.root.append(word)

    def search(self, word: str) -> bool:
        if word in self.root:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.root:
            if prefix in word:
                return True
        return False
        