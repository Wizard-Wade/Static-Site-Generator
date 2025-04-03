import unittest
from leafnode import LeafNode

test_props = {"href":"https://www.google.com", "target": "_blank"}

class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("p", "Hello, world!", test_props)
        self.assertEqual(node.to_html(), r'<p href="https://www.google.com" target="_blank">Hello, world!</p>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")


