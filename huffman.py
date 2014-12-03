class Leaf(object):
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight


class Node(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.symbol = left.symbol + right.symbol
        self.weight = left.weight + right.weight


class HuffTree(object):
    """ Takes a already constructed HuffTree and encodes/decodes strings

    Take a look at SICP 2.3.4 for what I implemented or just goole wikipedia
    for a general overview

    Methods of interest:
        encode
        decode
    """
    def __init__(self, tree=None, dict=None, tuple_list=None):
        if dict is not None:
            tuples = [(k, v) for k, v in dict.items()]
            self.tree = self._make_tree(tuples)
        elif tuple_list is not None:
            self.tree = self._make_tree(tuple_list)
        else:
            self.tree = tree

    # DECODE
    def decode(self, bits):
        """Decodes a Huffman Binary into a message

        Returns:
            decoded str eg. "Hello World"
        """
        return self._decode(bits, self.tree)

    def _decode(self, bits, current_branch):
        """Recursively calls itself to decode bits

        A helper method that uses recursiong and implicit state to recursively
        call itself and find bits to encode a message with

        Returns:
            function call or char eg. "H"
        """
        if bits is '':
            return ''
        else:
            next_branch = self._choose_branch(bits[0], current_branch)
            if type(next_branch) is Leaf:
                return (next_branch.symbol +
                        self._decode(bits[1:], self.tree))
            else:
                return self._decode(bits[1:], next_branch)

    @staticmethod
    def _choose_branch(bit, branch):
        """Chooses branch based on Huffman Tree

        Short sweet lookup the splits in a Huffman tree

        Returns:
            Node or Leaf
        """
        if bit is '0':
            return branch.left
        elif bit is '1':
            return branch.right

    # ENCODE
    def encode(self, message):
        """Encodes message in Huffman Binary

        This method is the aggregation of multiple encode_symbol calls

        Returns:
            concated binary str eg. "01000101011001"

            note: returns a variable length binary
        """
        if message is '':
            return ''

        encoded = ''
        for symbol in message:
            encoded += self._encode_symbol(symbol)
        return encoded

    def _encode_symbol(self, symbol):
        """Walks the tree and finds the symbol then returns its binary string

        Returns:
            binary str eg. "010"

            note: returns a variable length binary
        """
        queue = []
        queue.append(('', self.tree))
        while queue:
            path, struct = queue.pop(0)
            if type(struct) is Node:
                queue.append((path+'0', struct.left))
                queue.append((path+'1', struct.right))
            else:
                if struct.symbol is symbol:
                    return path

    def _make_tree(self, tuples):
        leaves = [Leaf(symbol, weight) for symbol, weight in tuples]
        # Sort the list in alphabetical order to for tie-breaking equal weights
        alphabetical = sorted(leaves, key=lambda x: x.symbol, reverse=True)
        tree = self._merge(alphabetical)
        return tree

    def _merge(self, nodes):
        if len(nodes) >= 2:
            desc_list = sorted(nodes, key=lambda x: x.weight, reverse=True)
            second, last = desc_list[-2:]

            if len(nodes) > 2:
                lead = desc_list[:-2]
                return self._merge(lead + [Node(second, last)])

            elif len(nodes) == 2:
                # Wrap final nodes in a node
                return Node(second, last)

        else:  # This should never happen
            return nodes


sample_dict = {
    "a": 4,
    "c": 1,
    "b": 2,
    "d": 1
}
