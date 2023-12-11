import pandas as pd
import os

def limpiar_consola():
    os.system("cls")

limpiar_consola()

# Crear un DataFrame con datos médicos, enfermedades y cirugías previas
datos_medicos = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Carlos', 'Laura', 'Roberto', 'Sofía', 'Paciente1', 'Paciente2', 'Paciente3'],
    'Edad': [35, 28, 45, 32, 40, 33, 55, 28, 60, 58, 57],
    'Altura (cm)': [170, 160, 175, 162, 180, 155, 165, 170, 175, 168, 170],
    'Presión Arterial': ['120/80', '130/85', '140/90', '110/75', '125/82', '135/88', '130/85', '120/78', '140/90', '130/85', '135/88'],
    'Enfermedad': ['Hipertensión', 'Ninguna', 'Diabetes', 'Asma', 'Ninguna', 'Hipertensión', 'Diabetes', 'Ninguna', 'Coronaria', 'Coronaria', 'Coronaria'],
    'Cirugias_Previas': ['Ninguna', 'Apéndice', 'Ninguna', 'Cataratas', 'Ninguna', 'Ninguna', 'Bypass', 'Ninguna', 'Ninguna', 'Vesícula', 'ByPass']
}

df_medico = pd.DataFrame(datos_medicos)

# Generar rango de edad de 10 años hasta los 90 años
rango_edad = list(range(0, 91, 10))
df_medico['Grupo_Edad'] = pd.cut(df_medico['Edad'], bins=rango_edad, labels=[f'{i}-{i+9}' for i in rango_edad[:-1]])

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

# Calcular la incidencia de enfermedades por grupo de edad
incidencia_por_grupo_edad = df_medico.groupby('Grupo_Edad')['Enfermedad'].value_counts().unstack().fillna(0)
print("Incidencia de enfermedades por grupo de edad:")
print(incidencia_por_grupo_edad)
print()

# Calcular la incidencia de cirugías previas por grupo de edad
incidencia_cirugias_por_grupo_edad = df_medico.groupby('Grupo_Edad')['Cirugias_Previas'].value_counts().unstack().fillna(0)
print("Incidencia de cirugías previas por grupo de edad:")
print(incidencia_cirugias_por_grupo_edad)
