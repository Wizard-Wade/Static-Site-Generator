import markdown_to_html
import shutil
import os

def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        from_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), from_path)
        if not os.path.exists(from_path):
            raise Exception("Could not find markdown content")
    
    if not os.path.exists(template_path):
        template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), template_path)
        if not os.path.exists(template_path):
            raise Exception("Could not find template")
    
    if not os.path.exists(os.path.dirname(dest_path)):
        dest_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dest_path)
        if not os.path.exists(os.path.dirname(dest_path)):
            raise Exception("Destination folder does not exist")

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as md_file:
        md = md_file.read()
    html = markdown_to_html.markdown_to_html_node(md).to_html()
    heading = markdown_to_html.extract_title(md)

    with open(template_path, 'r') as template_file:
        template = template_file.read()
    webpage_html = template.replace(r"{{ Title }}", heading).replace(r"{{ Content }}", html)

    with open(dest_path, 'w') as webpage:
        webpage.write(webpage_html)