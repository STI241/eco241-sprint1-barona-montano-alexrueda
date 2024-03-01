import pandas as pd

def ordenar_dataframe(df, columna, tipo_orden):
    if tipo_orden.lower() == 'ascendente':
        df_ordenado = df.sort_values(by=columna, ascending=True)
    elif tipo_orden.lower() == 'descendente':
        df_ordenado = df.sort_values(by=columna, ascending=False)
    
    return df_ordenado

data = pd.read_csv('data.csv')

columna = input('Ingrese el nombre de la columna por la cual desea ordenar (Edad, Hermanos, DeportesPracticados, CreditosCursados, Estrato, ExpectativaIngresos): ')

# Validar columna
while columna not in ['Edad', 'Hermanos', 'DeportesPracticados', 'CreditosCursados', 'Estrato', 'ExpectativaIngresos']:
    print("Nombre de columna no válido. Por favor, elija entre 'Edad', 'Hermanos', 'DeportesPracticados', 'CreditosCursados', 'Estrato', 'ExpectativaIngresos'.")
    columna = input('Ingrese el nombre de la columna por la cual desea ordenar: ')

tipo_orden = input('Ingrese el tipo de ordenamiento (ascendente o descendente): ')

# Validar tipo de ordenamiento
while tipo_orden.lower() not in ['ascendente', 'descendente']:
    print("Tipo de ordenamiento no válido. Por favor, elija 'ascendente' o 'descendente'.")
    tipo_orden = input('Ingrese el tipo de ordenamiento (ascendente o descendente): ')

print(f'Seleccionó {columna} en orden {tipo_orden}')
df_ordenado = ordenar_dataframe(data, columna, tipo_orden)
print("Datos ordenados:")
print(df_ordenado[['Id', columna]])
