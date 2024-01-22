import inspect
import modulo_inspect


sig = inspect.signature(modulo_inspect.module_level_function)
print(f'module_level_function {sig}')
# Codigo para validar que tipo de parametros hay.
print('\nParameter details:')
# Aca iteramos (inspecionar) sobre sig ()
for name, param in sig.parameters.items():
    if param.kind == inspect.Parameter.KEYWORD_ONLY:
        print(f' {name} (positional-only)')
    elif param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
        if param.default != inspect.Parameter.empty:
            print(f"    {name} = '{param.default}'")
        else:
            print(f'    {name}')
    elif param.kind == inspect.Parameter.VAR_POSITIONAL:
        print(f'    {name}')
    elif param.kind == inspect.Parameter.KEYWORD_ONLY:
        if param.default != inspect.Parameter.empty:
            print(f'        {name} = {param.default}')
        else:
            print(f'        {name} (Keyword-only)')
    elif param.kind == inspect.Parameter.VAR_KEYWORD:
        print(f'     **{name}')


print('-- Decoradores')


_sig = inspect.signature(modulo_inspect.module_level_function)

bound = _sig.bind(
    'this is arg1',
    'this is arg2',
    'this is an extra positional argument',
    extra_named_arg='value',
)

print('Arguments: ')


for name, value in bound.arguments.items():
    print(f'{name} = {value}')

print('\nCallin: ')
print(modulo_inspect.module_level_function(*bound.args, **bound.kwargs))


print('-- Agregar otros elementos -- '.upper())


sig__ = inspect.signature(modulo_inspect.module_level_function)

partial = sig.bind_partial(
    'this is arg1,'
    'this is arg2'
)

print('-- Whithout defaults: ')
for name, value in partial.arguments.items():
    print(f' {name} = {value}')


print('\n--With defaults: ')
partial.apply_defaults()
for name, value in partial.arguments.items():
    print(f'{name} = {value}')

print('-- Inspeccion dinamica')


sig_ = inspect.signature(modulo_inspect.ejemplo_funccion)

# Obtenemos la lista detallada de la funcion
for name, param in sig_.parameters.items():
    print(f'Nombre: {name}, Tipo: {param.annotation}, Prede: {param.default}')


print('-- Obtenr la firma de una funcion')


def ejemplo_fun(paramUno: int, paramDos: str = 'default'):
    return 3.14


signature_ = inspect.signature(ejemplo_fun)
print(signature_)


print('-- Asginar mas de un valor')


# Asignaremos valores a mas de una parametros
def funcion(arg1, arg2='default_value', arg3=42):
    return f'arg1: {arg1}, arg2: {arg2}, arg3: {arg3}'


# Obtenemos la firma de la funcion. Los valores predetermiandos
signatu = inspect.signature(funcion)
print(f'Obtenemos la firma: {signatu}')

parcial = signatu.bind_partial('arg1', arg2='valor2', arg3=99)


print('-- Valores, tipo de valores')
for name, value in signatu.parameters.items():
    print(f'Nombre: {name}, Tipo: {value.annotation}, predeterminado: {value.default}')

print('-- Valores por defecto')
# Aca imprimimos los parametros por predeterminados
for name, value in signatu.parameters.items():
    print(f' {name} = {value}')


print('\nCon valores predeterminados y aplicados')
parcial.apply_defaults()
for name, value in parcial.arguments.items():
    print(' {} = {}'.format(name, value))
