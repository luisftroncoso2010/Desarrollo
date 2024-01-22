import inspect
import modulo_inspect


# Creamoa las clases con las que se harán las jerarquias
class C(modulo_inspect.B):
    pass


class D(C, modulo_inspect.A):
    pass


# Creamos la funcion para iterar sobre la lista de clases
def print_class_tree(tree, indent=-1):
    # Validamos si es una instacia de la listas(Tree)
    if isinstance(tree, list):
        # Recorremos la lista
        for node in tree:
            # Hacemos la llamada recursiva.
            print_class_tree(node, indent + 1)
    else:
        print(' ' * indent, tree[0].__name__)
        return


if __name__ == '__main__':
    print('A, B, C, D:')
    print_class_tree(inspect.getclasstree(
        [modulo_inspect.A, modulo_inspect.B, C, D]))


mro_d = C.__mro__
print(mro_d)
