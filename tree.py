class treeNode:
    def __init__(self, parent, title: str = None, topics: list = None):
        self.name = title
        self.children = []
        self.parent = parent

        if topics:
            for topic in topics:
                if 'topics' in topic.keys():
                    self.add_child(treeNode(parent = self, title = topic['title'], topics = topic['topics']))
                else:
                    self.add_child(treeNode(parent = self, title = topic['title']))

    def add_child(self, child):
        self.children.append(child)
        return 
    
    def delete_childe(self, child):
        self.children.remove(child)
        return

    def get_name(self):
        return self.name
    
    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    def set_name(self, name):
        self.name = name
        return
    
class Tree:
    def __init__(self, data: dict):
        self.sheetname = data['title']
        self.topic = data['topic']
        if 'topics' in self.topic.keys():
            self.root = treeNode(parent = None, title = self.topic['title'], topics = self.topic['topics'])
        else:
            self.root = treeNode(parent = None, title = self.topic['title'])

    def print_tree(self):
        self.print_tree_helper(self.root)

    def print_tree_helper(self, node):
        print(node.get_name())
        for child in node.get_children():
            self.print_tree_helper(child)
        