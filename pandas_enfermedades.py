""" import pandas as pd
import os

def limpiar_consola():
    os.system("cls")

limpiar_consola()

# Crear un DataFrame con datos médicos y enfermedades
datos_medicos = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Carlos', 'Laura', 'Roberto', 'Sofía'],
    'Edad': [35, 28, 45, 32, 40, 33, 55, 28],
    'Altura (cm)': [170, 160, 175, 162, 180, 155, 165, 170],
    'Presión Arterial': ['120/80', '130/85', '140/90', '110/75', '125/82', '135/88', '130/85', '120/78'],
    'Enfermedad': ['Hipertensión', 'Ninguna', 'Diabetes', 'Asma', 'Ninguna', 'Hipertensión', 'Diabetes', 'Ninguna']
}

def limpiar_consola():
    os.system("cls")
    
limpiar_consola()


df_medico = pd.DataFrame(datos_medicos)

# Mostrar el DataFrame
print("Datos Médicos:")
print(df_medico)
print()

# Obtener estadísticas descriptivas
print("Estadísticas Descriptivas:")
print(df_medico.describe())
print()

# Filtrar por edad
print("Pacientes mayores de 30 años:")
mayores_de_30 = df_medico[df_medico['Edad'] > 30]
print(mayores_de_30)
print()

# Calcular la incidencia de enfermedades por edad
incidencia_por_edad = df_medico.groupby('Edad')['Enfermedad'].value_counts().unstack().fillna(0)
print("Incidencia de enfermedades por edad:")
print(incidencia_por_edad)
 """
 
import pandas as pd
import os

def limpiar_consola():
    os.system("cls")

limpiar_consola()

# Crear un DataFrame con datos médicos y enfermedades
datos_medicos = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Carlos', 'Laura', 'Roberto', 'Sofía', 'Paciente1', 'Paciente2', 'Paciente3'],
    'Edad': [35, 28, 45, 32, 40, 33, 55, 28, 60, 58, 57],
    'Altura (cm)': [170, 160, 175, 162, 180, 155, 165, 170, 175, 168, 170],
    'Presión Arterial': ['120/80', '130/85', '140/90', '110/75', '125/82', '135/88', '130/85', '120/78', '140/90', '130/85', '135/88'],
    'Enfermedad': ['Hipertensión', 'Ninguna', 'Diabetes', 'Asma', 'Ninguna', 'Hipertensión', 'Diabetes', 'Ninguna', 'Coronaria', 'Enfermedad Coronaria', 'ACV']
}

df_medico = pd.DataFrame(datos_medicos)

# Mostrar el DataFrame
print("Datos Médicos:")
print(df_medico)
print()

# Obtener estadísticas descriptivas
print("Estadísticas Descriptivas:")
print(df_medico.describe())
print()

# Filtrar por edad
print("Pacientes mayores de 30 años:")
mayores_de_30 = df_medico[df_medico['Edad'] > 30]
print(mayores_de_30)
print()

# Calcular la incidencia de enfermedades por edad
incidencia_por_edad = df_medico.groupby('Edad')['Enfermedad'].value_counts().unstack().fillna(0)
print("Incidencia de enfermedades por edad:")
print(incidencia_por_edad)
