from enum import Enum
from htmlnode import *

class TextType(Enum):
    text = "text"
    bold = "**"
    italic = "_"
    code = "`"
    link = "[*]"
    image = "!"

def text_node_to_html_node(textnode):
    match (textnode.text_type):
        case TextType.text:
            return LeafNode(None, textnode.text)
        case TextType.bold:
            return LeafNode("b", textnode.text)
        case TextType.italic:
            return LeafNode("i", textnode.text)
        case TextType.code:
            return LeafNode("code", textnode.text)
        case TextType.link:
            return LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.image:
            return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text} )

class Textnode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, textnode):
        return self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

