import os

#first delete all of the files in the public folder
#it should then copy all files and subdirectories nested files etc to the public folder.
#recommended to log the path of each file copied so we can see what's happening as we run and debug.

def delete_public_contents():
    public_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..//public")
    if not os.path.exists(public_path):
        os.mkdir(public_path)
        return
    
    delete_dir_files_(public_path)
    
def delete_dir_files_(dir_path):       
    for name in os.listdir(dir_path):
        fullpath = os.path.join(dir_path, name)
        if os.path.isfile(fullpath):
            os.remove(fullpath)
        else:
            delete_dir_files_(fullpath)
            os.removedirs(fullpath)

        
    

        

delete_public_contents()