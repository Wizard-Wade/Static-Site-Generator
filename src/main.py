from textnode import *

def main():
    node = Textnode("this is some anchor text", TextType.link, "https://www.boot.dev")
    print(node)
    

main()