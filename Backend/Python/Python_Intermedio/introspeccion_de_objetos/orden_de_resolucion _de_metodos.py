import inspect
import modulo_inspect


class C(object):
    pass


class C_First(C, modulo_inspect.B):
    pass


class B_First(modulo_inspect.B, C):
    pass


print('B_First: ')


for c in inspect.getmro(B_First):
    print(f' {c.__name__}')
print(' ')
print('C_First: ')
for c in inspect.getmro(C_First):
    print(f' {c.__name__}')
