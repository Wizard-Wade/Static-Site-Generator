from textnode import *
from htmlnode import *
from split_nodes import *

def main():
    node = Textnode("this is some anchor text", TextType.link, "https://www.boot.dev")
    node2 = Textnode("This is text with a **bolded phrase** in the middle", TextType.text)
    print(node)
    split_nodes_delimiter([node2],"**", TextType.bold)
    

main()