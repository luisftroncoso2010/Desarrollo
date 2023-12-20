'''Depurando: Ayudar si tenemos un bug o fallo que necesitamos
resolver. Depurador PDB'''
import pdb


def haz_algo():
    # Aca se le asigna un break poin o puntos de ruptura
    pdb.set_trace()
    return "No quiero"


print(haz_algo())
