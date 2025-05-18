from block_markdown import *
import htmlnode
import textnode
import inline_markdown

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        b_type = block_to_block_type(block)

        if b_type == BlockType.CODE:
            tnode = textnode.TextNode(block.lstrip("```\n").rstrip("```"), textnode.TextType.CODE)
            leaf_html = textnode.text_node_to_html_node(tnode)
            p_html = htmlnode.ParentNode("pre", [leaf_html])
            nodes.append(p_html)
            continue

        kids = []
        block_list = block_strip_styling(block, b_type)
        for sub_block in block_list:
            if sub_block is "":
                continue
            tnodes = inline_markdown.text_to_textnodes(sub_block)
            l_html = list(map(lambda x : textnode.text_node_to_html_node(x), tnodes))
            if b_type is BlockType.OLIST or b_type is BlockType.ULIST:
                kids.append(htmlnode.ParentNode("li", l_html))
            else:
                kids += l_html

        if b_type == BlockType.ULIST:
            tag = "ul"
        elif b_type == BlockType.OLIST:
            tag = "ol"
        elif b_type == BlockType.QUOTE:
            tag = "blockquote"
        elif b_type == BlockType.HEADING:
            f1 = block.split(" ", 1)[1]
            hlevel = len(block.split(" ", 1)[0])
            tag = f"h{hlevel}"
        else:
            tag = "p"
        pnode = htmlnode.ParentNode(tag=tag, children=kids)
        nodes.append(pnode)
    return htmlnode.ParentNode("div", nodes)

def extract_title(markdown):
    #find the header line
    blocks = markdown_to_blocks(markdown)
    
    heading = next((sub_block for sub_block in blocks if sub_block.startswith(r"# ")), None)
    if not heading:
        raise Exception("Could not find h1 heading")
    
    return block_strip_styling(heading, BlockType.HEADING)[0]
  