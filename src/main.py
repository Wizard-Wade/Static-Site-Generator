from textnode import *
from copy_static_to_public import generate_public_assets
from Generate_page import generate_page

def main():
    generate_public_assets()
    generate_page("..//content//index.md", "..//templates//template.html", "..//public//index.html")

main()