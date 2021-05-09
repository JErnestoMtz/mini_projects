class Node:
    def __init__(self,symbol, weight, left = None, right = None):
        self.symbol = symbol
        self.left = left
        self.right = right
        self.weight = weight
    def children(self):
        return (self.left, self.right)
    def __str__(self):
        return '%s_%s' % (self.left, self.right)

    
    def preorder_traversal(self, path = '', codes = {}): #depth traversal, preorder traversal
                                #<left><rigth><roo>
        if self.left == None:
            codes[self.symbol] = path
        else:
            self.left.preorder_traversal(path+'0', codes)
            self.right.preorder_traversal(path + '1', codes)
        return codes

def sort_by_weigth(node: Node):
    return (node.weight * 10000000 + ord(node.symbol[0]))


class huffman:
    def __init__(self, tree = None, source = None):
        None
    def gen_tree(self, source):
        freq = self.get_freq(source)
        print(freq)
        tree = [] # list of node with wight = freq
        for sym in freq.keys():
            tree.append(Node(sym, freq[sym]))
        tree.sort(key = sort_by_weigth)
        while len(tree)>1:
            l = tree.pop(0)
            r = tree.pop(0)
            new_node = Node(l.symbol + r.symbol,l.weight + r.weight, l,r)
            tree.append(new_node)
            tree.sort(key = sort_by_weigth) 
        return tree

    def encode(self, source , tree = None):
        if not tree:
            self.tree = self.gen_tree(source)
        else:
            self.tree = tree
        self.codes = self.tree[0].preorder_traversal()
        print(self.codes)
        encoded = ''
        for sym in source:
            encoded += self.codes[sym]
        return encoded
    def get_freq(self,string):
        #creates a dictionary with key beeingn each symbol and value the freq
        symbols = {}
        for sym in string:
            symbols[sym] = symbols.get(sym,0)+1
        return symbols

h = huffman().encode("lossless compression")
print(h)
