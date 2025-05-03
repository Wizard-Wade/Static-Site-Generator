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
            hlevel = len(block.split(" ", 1)[1])
            tag = f"H{hlevel}"
        else:
            tag = "p"
        pnode = htmlnode.ParentNode(tag=tag, children=kids)
        nodes.append(pnode)
        print(nodes)
    return htmlnode.ParentNode("div", nodes)

            

        #convert block to textnodes

def text_to_children(text):
    #take string of text and return HTML node
    pass
  