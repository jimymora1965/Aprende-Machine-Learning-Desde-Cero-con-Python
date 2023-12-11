import pandas as pd

def main():
    # Solicitar al usuario el rango de años
    año_inicio = int(input("Ingrese el año de inicio: "))
    año_fin = int(input("Ingrese el año de fin: "))

    # Crear un diccionario para almacenar las ventas por año
    ventas = {}

    # Recopilar las ventas para cada año en el rango especificado
    for año in range(año_inicio, año_fin + 1):
        venta_anual = float(input(f"Ingrese las ventas para el año {año}: "))
        ventas[año] = venta_anual

    # Crear una serie con los datos originales
    serie_original = pd.Series(ventas, name='Ventas Originales')

    # Aplicar un descuento del 10%
    serie_con_descuento = serie_original * 0.9

    # Crear un DataFrame para mostrar ambas series
    df = pd.DataFrame({'Ventas Originales': serie_original, 'Ventas con Descuento': serie_con_descuento})

    # Imprimir el DataFrame
    print("\nDatos de Ventas:")
    print(df)

if __name__ == "__main__":
    main()
