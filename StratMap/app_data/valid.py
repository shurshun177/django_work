from datetime import datetime as d
def is_valid_code(measure_code):
    d_1 = {'q': '', 'e': 5, 'u':'err'}
    t = '0123456789.'
    test_func = map(lambda x: x in t, measure_code)
    c = False not in test_func
    f = (i for i in d_1.values() if not i)

    return c, f
def is_valid_number(vers_number):
    return isinstance(vers_number, int)



#print(is_valid_number(234))