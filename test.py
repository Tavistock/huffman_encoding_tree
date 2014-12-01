import unittest

from huffman import Node, Leaf, HuffTree

sample_tree = Node(Leaf('a', 4),
                   Node(Leaf('b', 2),
                        Node(Leaf('d', 1), Leaf('c', 1))
                        )
                   )

sample_bits = "0110010101110"

sample_text = 'adabbca'


class MyTest(unittest.TestCase):
    def setUp(self):
        self.huff_tree = HuffTree(sample_tree)

    def test_encode(self):
        self.assertEqual(self.huff_tree.encode(sample_text), sample_bits)

    def test_decode(self):
        self.assertEqual(self.huff_tree.decode(sample_bits), sample_text)

# someday I may implement this
sample_dict = {
    "a": 4,
    "c": 1,
    "b": 2,
    "d": 1
}
