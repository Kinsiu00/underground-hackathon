# remove files in this directory
import os, shutil
folder = '../underground-hackathon'

for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    # print(file_path)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)