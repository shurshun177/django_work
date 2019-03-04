import json
import os
def entry(name, password):
    path = os.path.dirname(os.getcwd())
    with open(os.path.join(path,'users.json'), 'r') as f:
        d = f.read()
    j = json.loads(d)
    list_users = j.get('users')
    l = [i.get('type') for i in list_users if i.get('user') == name and i.get('password') == password]
    if l:
        print(l[0])
    else:
        print('No such user')
    return


'''''
    if j.get(name) == password:
        return {'status': 'accepted', 'user': name}
    else:
        return {'status': 'denied'}
if __name__ == '__main__':
    import os, sys
    # get an absolute path to the directory that contains mypackage
    foo_dir = os.path.dirname(os.path.join(os.getcwd(), __file__))
    sys.path.append(os.path.normpath(os.path.join(foo_dir, '..', '..')))
    from mypackage import bar
else:
    from .. import bar
'''''
# print(__file__)
foo_dir = os.path.dirname(os.path.join(os.getcwd(), __file__))
# print(foo_dir)
path = os.path.join(os.getcwd(), __file__)
# print(path)
normpath = os.path.normpath(os.path.join(os.getcwd(), __file__))
# print(normpath)
# print(os.path.dirname(os.getcwd()))
# entry('Artur', '1024512')