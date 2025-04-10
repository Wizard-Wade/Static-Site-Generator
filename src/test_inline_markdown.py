import unittest
from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import Textnode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = Textnode("This is text with a **bolded** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                Textnode("This is text with a ", TextType.text),
                Textnode("bolded", TextType.bold),
                Textnode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = Textnode(
            "This is text with a **bolded** word and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                Textnode("This is text with a ", TextType.text),
                Textnode("bolded", TextType.bold),
                Textnode(" word and ", TextType.text),
                Textnode("another", TextType.bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = Textnode(
            "This is text with a **bolded word** and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                Textnode("This is text with a ", TextType.text),
                Textnode("bolded word", TextType.bold),
                Textnode(" and ", TextType.text),
                Textnode("another", TextType.bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = Textnode("This is text with an _italic_ word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "_", TextType.italic)
        self.assertListEqual(
            [
                Textnode("This is text with an ", TextType.text),
                Textnode("italic", TextType.italic),
                Textnode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = Textnode("**bold** and _italic_", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.italic)
        self.assertListEqual(
            [
                Textnode("bold", TextType.bold),
                Textnode(" and ", TextType.text),
                Textnode("italic", TextType.italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = Textnode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        self.assertListEqual(
            [
                Textnode("This is text with a ", TextType.text),
                Textnode("code block", TextType.code),
                Textnode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_spliterror(self):
        node = Textnode("This is text with a **bolded phrase in the middle", TextType.text)
        self.assertRaises(Exception, split_nodes_delimiter, ([node], "**", TextType.bold))
        
    def test_startbold(self):
        node = Textnode("**bolded phrase** is at the start", TextType.text)
        self.assertRaises(Exception, split_nodes_delimiter, ([node], "**", TextType.bold))


if __name__ == "__main__":
    unittest.main()