import unittest
from htmlnode import HTMLNode

test_tag = "<p>"
test_props = {"href":"https://www.google.com", "target": "_blank"}

class TestHtmlNode(unittest.TestCase):
    #create a self.test properities for each case, then test various bits
    def testprint(self):
        node=HTMLNode(tag = test_tag, props=test_props)
        self.assertEqual(repr(node), r"('tag', '<p>'), ('props', {'href': 'https://www.google.com', 'target': '_blank'}), ")
    
    def testprops(self):
        node=HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(),r' href="https://www.google.com" target="_blank"')

    def testprops(self):
        node=HTMLNode(props=test_props)
        self.assertNotEqual(node.props_to_html(),r'href="https://www.google.com" target="_blank"')
    
