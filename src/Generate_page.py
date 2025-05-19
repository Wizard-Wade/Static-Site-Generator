import markdown_to_html
import shutil
import os
import pathlib

def generate_website(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        dir_path_content = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir_path_content)
        if not os.path.exists(dir_path_content):
            raise Exception("Could not find content folder")
    
    if not os.path.exists(dest_dir_path):
        dest_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dest_dir_path)
        if not os.path.exists(dest_dir_path):
            raise Exception("Destination folder does not exist")
        
    if not os.path.exists(template_path):
        template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), template_path)
        if not os.path.exists(template_path):
            raise Exception("Could not find template")
    
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
    
    
def generate_pages_recursive(dir_path, template_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for name in os.listdir(dir_path):
        s_fullpath = os.path.join(dir_path, name)
        d_fullpath = os.path.join(dest_path, name)
        if os.path.isfile(s_fullpath):
            generate_page(s_fullpath, template_path,  pathlib.Path(d_fullpath).with_suffix(".html"))
        else:
            os.mkdir(d_fullpath)
            generate_pages_recursive(s_fullpath, template_path, d_fullpath)

def generate_page(from_path, template_path, dest_path):

    if not os.path.exists(from_path):
        from_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), from_path)
        if not os.path.exists(from_path):
            raise Exception("Could not find content folder")
    
    if not os.path.exists(os.path.dirname(dest_path)):
        dest_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dest_path)
        if not os.path.exists(os.path.dirname(dest_path)):
            raise Exception("Destination folder does not exist")
        
    if not os.path.exists(template_path):
        template_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), template_path)
        if not os.path.exists(template_path):
            raise Exception("Could not find template")

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