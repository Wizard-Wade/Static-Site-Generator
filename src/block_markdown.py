from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = '""'
    HEADING = "#"
    CODE = "```"
    QUOTE = ">"
    ULIST = "-"
    OLIST = "*. "

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        block = block.strip()
        if block:
            filtered.append(block)
    return filtered

def block_to_block_type(block):
    if block.count(" ") > 0:
        first_word, *mid, last_word = block.split()
    else:
        first_word = block
        last_word = block

    if first_word.startswith(BlockType.HEADING.value):
        return BlockType.HEADING
    if first_word.startswith(BlockType.CODE.value) and last_word.endswith(BlockType.CODE.value):
        return BlockType.CODE
    split_lines =  block.split("\n")
    if all(list(map(lambda x: x.startswith(BlockType.QUOTE.value), split_lines))):
        return BlockType.QUOTE 
    if all(list(map(lambda x: x.startswith(BlockType.ULIST.value), split_lines))):
        return BlockType.ULIST  
    for i in range(len(split_lines)):
        if not split_lines[i].startswith(f"{i+1}. "):
            break
        if i == len(split_lines) -1:
            return BlockType.OLIST
    return BlockType.PARAGRAPH

def block_strip_styling(block, block_type):
    if block_type == BlockType.ULIST:
        blocks = block_split_unordered_list(block)
    elif block_type == BlockType.OLIST:
        blocks = block_split_ordered_list(block)
    else:
        blocks = [block.strip(block_type.value).strip()]
    return list(map(lambda x: x.replace("\n", " "),blocks))

def block_split_ordered_list(block):
    return re.split(r"^(\d[.])",block).strip()

def block_split_unordered_list(block):
    return re.split(r"^(-)",block).strip()
