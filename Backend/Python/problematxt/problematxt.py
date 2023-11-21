'''
Se desea crear dos listas, una con nombres y otra con apellidos
'''
nombres = ['Lucas', 'Matias', 'Leonardo', 'Luis', 'Juan']
apellidos = ['Troncoso', 'Montes', 'Alvares', 'Jimenez', 'Belgrano']
#Registrar toda esta informacion de forma optina
with open("Backend//Python//problematxt//problema.txt", 'w') as arch:
    arch.writelines("Los datos son:\n\n")    
    [arch.writelines(f'nombre: {n}\nApellido: {a}\n-------------\n' for n, a in zip(nombres, apellidos))]