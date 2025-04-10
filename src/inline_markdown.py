from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    l1 = []
    for node in old_nodes:
        if node.text_type is not TextType.text or delimiter not in node.text:
            l1.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax")
        fragments = node.text.split(delimiter)
        print(fragments)
        l2 = []
        for (i,fragment) in enumerate(fragments):
            if fragment == "":
                continue
            if i % 2 == 0:
                l2.append(Textnode(fragment,TextType.text))
            else:
                l2.append(Textnode(fragment, text_type))
        l1.extend(l2)
    print(l1)
    return l1
                
   