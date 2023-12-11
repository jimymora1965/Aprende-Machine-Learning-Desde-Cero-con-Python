# import pandas as pd

# # Crear una lista del 1 al 10
# datos = list(range(1, 11))

# # Crear una serie con la lista y asignar letras como índices
# serie = pd.Series(datos, index=list('abcdefghij'))

# # Imprimir la serie
# print(serie)

import pandas as pd

# Solicitar la cantidad de números
cantidad_numeros = int(input("Ingrese la cantidad de números: "))

# Crear una lista del 1 al cantidad_numeros
datos = list(range(1, cantidad_numeros + 1))

# Crear una serie con la lista y asignar letras como índices
serie = pd.Series(datos, index=list(chr(i) for i in range(97, 97 + cantidad_numeros)))

# Imprimir la serie
print(serie)
