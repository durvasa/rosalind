def FASTA_iterator(fasta_filename):

    """
    A generator function that reads a FASTA file. At each iteration, the
    function must return a tuple with the format (identifier, sequence).
    """

    with open(fasta_filename, 'rt') as fasta:
        sequence = ''
        identifier = ''
        my_list = []
        for line in fasta:
            if (line[0] == '>'):
                if (sequence != ''):
                    my_tuple = (identifier, sequence)
                    yield(my_tuple)
                    identifier= ''
                    sequence= ''
                identifier = line[1:].strip()
            else:
                sequence += line.strip()
        my_tuple = (identifier, sequence)
        yield(my_tuple)


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if graph[start] == set():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

#### IMPLEMENTATION OF A TREE ####

class Node(object):
    
    def __init__(self, label):
        self.label = label
        self.parent = None
        self.children = set()
    
    def add_child(self, node):
        self.children.add(node)
        node.parent = self

class Tree(object):
    
    def __init__(self, root):
        self.root = root
    
    def tree_dict(self):
        mydict = {}
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            mydict[node.label] = set()
            for child in node.children:
                queue.append(child)
                mydict[node.label].add(child.label)
        return mydict
    
    def graph_dict(self):
        mydict = self.tree_dict()
        for key in mydict:
            for child in mydict[key]:
                mydict[child].add(key)
        return mydict
    
    def find_all_paths(self, start_label, end_label, path=[]):
        graph = self.graph_dict()
        path = path + [start_label]
        if start_label == end_label:
            return [path]
        if graph[start_label] == set():
            return []
        paths = []
        for node in graph[start_label]:
            if node not in path:
                newpaths = self.find_all_paths(node, end_label, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
    def distance(self, start_label, end_label):
        paths = self.find_all_paths(start_label, end_label)
        l = paths.pop()
        return len(l) - 1




