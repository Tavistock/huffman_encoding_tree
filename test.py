import unittest

from huffman import Node, Leaf, HuffTree

sample_tree = Node(Leaf('a', 4),
                   Node(Leaf('b', 2),
                        Node(Leaf('d', 1), Leaf('c', 1))
                        )
                   )

sample_bits = "0110010101110"

sample_text = 'adabbca'

sample_dict = {
    "a": 4,
    "c": 1,
    "b": 2,
    "d": 1
}


class FromTree(unittest.TestCase):
    def setUp(self):
        self.huff_tree = HuffTree(sample_tree)

    def test_encode(self):
        self.assertEqual(self.huff_tree.encode(sample_text), sample_bits)

    def test_decode(self):
        self.assertEqual(self.huff_tree.decode(sample_bits), sample_text)


class FromDict(unittest.TestCase):

    def setUp(self):
        self.huff_tree = HuffTree(dict=sample_dict)

    def test_encode(self):
        self.assertEqual(self.huff_tree.encode(sample_text), sample_bits)

    def test_decode(self):
        self.assertEqual(self.huff_tree.decode(sample_bits), sample_text)
