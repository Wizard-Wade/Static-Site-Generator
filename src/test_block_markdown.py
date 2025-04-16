import unittest
from block_markdown import *


class TestblockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """# This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self .assertEqual(
            blocks,
            [
                "# This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        types = list(map(lambda block: block_to_block_type(block), blocks))
        self.assertEqual(types, [BlockType.HEADING, BlockType.PARAGRAPH, BlockType.UNORDERED_LIST])

    def test_markdown_to_blocks_newlines(self):
        md = """
## This is **bolded** paragraph




```This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line```

1. This is a list
2. with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "## This is **bolded** paragraph",
                "```This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line```",
                "1. This is a list\n2. with items",
            ],
        )
        types = list(map(lambda block: block_to_block_type(block), blocks))
        self.assertEqual(types, [BlockType.HEADING, BlockType.CODE, BlockType.ORDERED_LIST])

if __name__ == "__main__":
    unittest.main()