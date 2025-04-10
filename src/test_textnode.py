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

    def test_to_html(self):
        node = Textnode("This is a text node", TextType.text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = Textnode("This is bold", TextType.bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_image(self):
        node = Textnode("This is an image", TextType.image, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )


        

if __name__ == "__main__":
    unittest.main()