import os.path
import re
import sys

path = sys.argv[1]
if os.path.exists(path):
    file = open(path, "r")
    for line in file:
        if "mapped" in line:
            data = re.findall(r'(\d+(?:\.\d+)?%)', line)
            print(data[0])
            float = float(data[0].strip('%'))/100
            if float > 0.9:
                print("OK")
            else:
                print("Not OK")
            break

else:
    print("file " + path + " does not exist")
