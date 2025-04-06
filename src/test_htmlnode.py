import unittest
from htmlnode import *

test_tag = "p"
test_value="Hello, world!"
test_props = {"href":"https://www.google.com", "target": "_blank"}

class TestHtmlNode(unittest.TestCase):
    #create a self.test properities for each case, then test various bits
    def testprint(self):
        node=HTMLNode(test_tag, test_value, props=test_props)
        leaf=LeafNode(test_tag,test_value,test_props)
        parent=ParentNode(test_tag, leaf)
        self.assertEqual(repr(node), r"HTMLNode(p, Hello, world!, children: None, {'href': 'https://www.google.com', 'target': '_blank'})")
        self.assertEqual(repr(leaf), r"LeafNode(p, Hello, world!, children: None, {'href': 'https://www.google.com', 'target': '_blank'})")
        self.assertEqual(repr(parent), f"ParentNode(p, None, children: {repr(leaf)}, None)")

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def testprops(self):
        node=HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(),r' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_no_value(self):
        node = LeafNode(test_tag, None, test_props)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
        

    
if __name__ == "__main__":
    unittest.main()
