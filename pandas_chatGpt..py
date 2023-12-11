import pandas as pd
import os

# Crear un DataFrame desde un diccionario de datos
datos = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 22, 28],
    'Ciudad': ['Ciudad A', 'Ciudad B', 'Ciudad A', 'Ciudad C']
}
def limpiar_consola():
    os.system("cls")
    
limpiar_consola()

df = pd.DataFrame(datos)

# Mostrar el DataFrame
print("DataFrame:")
print(df)
print()

# Obtener estadísticas descriptivas
print("Estadísticas descriptivas:")
print(df.describe())
print()

# Filtrar por edad
print("Personas mayores de 25 años:")
mayores_de_25 = df[df['Edad'] > 25]
print(mayores_de_25)
