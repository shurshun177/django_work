import sys
import os
import json


def read_j():

    cwd = os.getcwd()
    file_name = sys.argv[1]
    j = {}
    try:
        print('vot')
        with open(os.path.join(cwd, file_name), 'r') as f:
            d = f.read()
            j = json.loads(d)
            print(j)
    except:
        print('noviy povorot')
        print('No such file, try another filename')
    return j

def write_j():
    cwd = os.getcwd()
    file_name = 'buffer.json'
    j = read_j()
    try:

        with open(os.path.join(cwd, file_name), 'w') as f:

            data = json.dumps(j)
            f.write(data)
    except:

        print('No such file, try another filename')
    return


# read_j()
write_j()