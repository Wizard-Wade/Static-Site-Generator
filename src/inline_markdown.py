from textnode import *
import re

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    fragments = split_nodes_image([node])
    fragments = split_nodes_link(fragments)
    types = list(TextType)
    types.remove(TextType.TEXT)
    types.remove(TextType.IMAGE)
    types.remove(TextType.LINK)
    for type in types:
        fragments = split_nodes_delimiter(fragments, type)
    return fragments

def split_nodes_delimiter(old_nodes, text_type):
    delimiter = text_type.value
    l1 = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT or delimiter not in node.text:
            l1.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax")
        fragments = node.text.split(delimiter)
        l2 = []
        for (i,fragment) in enumerate(fragments):
            if fragment == "":
                continue
            if i % 2 == 0:
                l2.append(TextNode(fragment,TextType.TEXT))
            else:
                l2.append(TextNode(fragment, text_type))
        l1.extend(l2)
    return l1

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if not images:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if not links:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    if match:
        return match

def extract_markdown_links(text):
    match = re.findall(r"(?<!!)\[(.*?)\]\((\/.*?)\)", text)
    if match:
        return match

