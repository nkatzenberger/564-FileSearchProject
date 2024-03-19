# import required module
import os

# assign directory
dir = 'venv'

want = "test.txt"
# iterate over files in
# that directory

def filesFind(directory, target):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            if(filename == target):
                print("Found file at " + directory)
        else:
            filesFind(f, target)

filesFind(dir, want)