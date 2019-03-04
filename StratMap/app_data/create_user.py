import json
import os

def read():
    user_dict = {}
    cwd = os.path.dirname(os.getcwd())
    # print(cwd)
    try:
        with open(os.path.join(cwd, r'users.json'), 'r') as f:
            data_before = f.read()
            user_dict = json.loads(data_before)
    except:

        print('Netu')
    return user_dict


def create(name, password, type):
    cwd = os.path.dirname(os.getcwd())
    d = read()

    new_user = {
        'user': name,
        'password': password,
        'type': type
    }
    d['users'].append(new_user)
    with open(os.path.join(cwd, r'users.json'), 'w') as f:
        data = json.dumps(d)
        f.write(data)

# print(read())
create('Artur', '225625', 'מנהל מערכת')