import os

class Node:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path) if os.path.basename(path) else path

    def document(self, prefix='', is_last=True):
        raise NotImplementedError("Debe ser implementado por subclases.")

class DirectoryNode(Node):
    def __init__(self, path):
        super().__init__(path)
        self.children = []

    def document(self, prefix='', is_last=True):
        connector = "└── " if is_last else "├── "
        print(prefix + connector + self.name)
        new_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(self.children):
            child_is_last = i == len(self.children) - 1
            child.document(new_prefix, child_is_last)

class FileNode(Node):
    def document(self, prefix='', is_last=True):
        connector = "└── " if is_last else "├── "
        print(prefix + connector + self.name)
