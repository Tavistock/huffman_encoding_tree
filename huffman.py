from operator import itemgetter


class Leaf(object):
    """docstring for Leaf"""
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight


class Node(object):
    """
    """
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        # self.symbols = self.get_symbols(left) + self.get_symbols(right)
        # self.weight = left.weight + right.weight

    def get_symbols(self, tree):
        if type(tree) is Leaf:
            return [tree.symbol]
        else:
            return tree.symbols


class HuffTree(object):
    """docstring for HuffTree"""
    def __init__(self, freq_dict=None, tree=None):
        if freq_dict is not None:
            sorted_tuples = sorted(freq_dict.items(),
                                   reverse=True,
                                   key=itemgetter(1))
            self.tree = self._make_tree(sorted_tuples)
        else:
            self.tree = tree

    def decode(self, bits):
        return self._decode(bits, self.tree)

    def _decode(self, bits, current_branch):
        if bits is '':
            return ''
        else:
            next_branch = self.choose_branch(bits[0],
                                             current_branch)
            if type(next_branch) is Leaf:
                return (next_branch.symbol +
                        self._decode(bits[1:], self.tree))
            else:
                return self._decode(bits[1:], next_branch)

    @staticmethod
    def choose_branch(bit, branch):
        if bit is '0':
            return branch.left
        elif bit is '1':
            return branch.right


sample_dict = {
    "a": 4,
    "c": 1,
    "b": 2,
    "d": 1
}

sample_tree = Node(Leaf('a', 4),
                   Node(Leaf('b', 2),
                        Node(Leaf('d', 1), Leaf('c', 1))
                        )
                   )

sample_encode = "0110010101110"
