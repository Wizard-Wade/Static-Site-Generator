import os

#first delete all of the files in the public folder
#it should then copy all files and subdirectories nested files etc to the public folder.
#recommended to log the path of each file copied so we can see what's happening as we run and debug.

def delete_public_contents():
    public_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"public")
    if not os.path.exists(public_path):
        os.mkdir(public_path)
        return
    
    
    for dir in os.listdir(public_path):
        os.remove
    

        

delete_public_contents()