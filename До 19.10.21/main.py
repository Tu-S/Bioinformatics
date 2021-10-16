import os.path
import re
import sys

path = sys.argv[1]
if os.path.exists(path):
    file = open(path, "r")
    for line in file:
        if "mapped" in line:
            data = re.findall(r'(\d+(?:\.\d+)?%)', line)
            float = float(data[0].strip('%'))/100
            print(float)
            break

else:
    sys.exit(2)
