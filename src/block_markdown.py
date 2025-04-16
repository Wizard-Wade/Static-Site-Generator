from enum import Enum

class BlockType(Enum):
    PARAGRAPH = '""'
    HEADING = "#"
    CODE = "```"
    QUOTE = ">"
    UNORDERED_LIST = "-"
    ORDERED_LIST = "*. "

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        block = block.strip()
        if block:
            filtered.append(block)
    return filtered

def block_to_block_type(block):
    first_word, *mid, last_word = block.split()
    if first_word.startswith(BlockType.HEADING.value):
        return BlockType.HEADING
    if first_word.startswith(BlockType.CODE.value) and last_word.endswith(BlockType.CODE.value):
        return BlockType.CODE
    split_lines =  block.split("\n")
    if all(list(map(lambda x: x.startswith(BlockType.QUOTE.value), split_lines))):
        return BlockType.QUOTE 
    if all(list(map(lambda x: x.startswith(BlockType.UNORDERED_LIST.value), split_lines))):
        return BlockType.UNORDERED_LIST
    for i in range(len(split_lines)):
        if not split_lines[i].startswith(f"{i+1}. "):
            break
        if i == len(split_lines) -1:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
