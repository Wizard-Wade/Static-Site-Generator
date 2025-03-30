import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = Textnode("This is a text node", TextType.bold)
        node2 = Textnode("This is a text node", TextType.bold)
        self.assertEqual(node,node2)
    def test_neqt(self):
        node = Textnode("This is a different text node", TextType.bold)
        node2 = Textnode("This is a text node", TextType.bold)
        self.assertNotEqual(node,node2)
    def test_nequrl(self):
        node = Textnode("This is a text node", TextType.bold, "blankurl")
        node2 = Textnode("This is a text node", TextType.bold)
        self.assertNotEqual(node,node2)
    def test_neqType(self):
        node = Textnode("This is a text node", TextType.italic)
        node2 = Textnode("This is a text node", TextType.bold)
        self.assertNotEqual(node,node2)
        

if __name__ == "__main__":
    unittest.main()