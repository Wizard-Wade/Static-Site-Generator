import os
import shutil

#first delete all of the files in the public folder
#it should then copy all files and subdirectories nested files etc to the public folder.
#recommended to log the path of each file copied so we can see what's happening as we run and debug.

def delete_public_contents():
    public_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..//public")
    if os.path.exists(public_path):
        delete_dir_files_(public_path)
    
def delete_dir_files_(dir_path):      
    shutil.rmtree(dir_path)

def copy_static_contents():
    public_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..//public")
    static_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..//static")
    copy_dir_files_recursive(static_path, public_path)  
    
def copy_dir_files_recursive(src_path, dest_path): 
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for name in os.listdir(src_path):
        s_fullpath = os.path.join(src_path, name)
        d_fullpath = os.path.join(dest_path, name)
        if os.path.isfile(s_fullpath):
            shutil.copy(s_fullpath, d_fullpath)
        else:
            os.mkdir(d_fullpath)
            copy_dir_files_recursive(s_fullpath, d_fullpath)
    
    
def generate_public_assets():
    delete_public_contents()
    copy_static_contents()