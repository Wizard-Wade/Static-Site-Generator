from textnode import *
from copy_static import generate_assets
from Generate_page import generate_website, generate_page
import sys

def main():
    basepath = sys.argv[1] if len(sys.argv)> 1 else "/"
    generate_assets("docs")
    generate_website(f"..//content", f"..//templates//template.html", f"..//docs", basepath)

main()