import pandas as pd
#% pip install xlrd

# Especifica la ruta de tu archivo Excel
ruta_excel = "C:/Users/jpcan/OneDrive/Documentos/Andes Universidad/Analitica computacional/Proyecto 2/Copia de default of credit card clients.xls"

# Lee el archivo Excel en un DataFrame de pandas
datos_excel = pd.read_excel(ruta_excel, sheet_name="Data")

datos_excel.columns = datos_excel.iloc[0]

# Elimina la primera fila, ya que ahora son los nombres de las columnas
datos_excel = datos_excel[1:]


import pandas as pd

# Supongamos que 'df' es tu DataFrame
# df = pd.read_excel("ruta/a/tu/archivo.xlsx")

# Verifica si hay valores faltantes en cada columna
valores_faltantes_por_columna = datos_excel.isna().sum()

# También puedes usar df.isnull().sum() para el mismo propósito

import pandas as pd

# Supongamos que 'datos_excel' es tu DataFrame
# datos_excel = pd.read_excel("ruta/a/tu/archivo.xlsx")


# Eliminar filas con valores atípicos en la columna "EDUCATION"
datos_excel = datos_excel[datos_excel['EDUCATION'].isin([1, 2, 3, 4])]

# Eliminar filas con valores atípicos en la columna "MARRIAGE"
datos_excel = datos_excel[datos_excel['MARRIAGE'].isin([1, 2, 3])]

# Reindexar el DataFrame si es necesario
datos_excel.reset_index(drop=True, inplace=True)

# Cambiar el nombre de la columna "PAY_0" a "PAY_1"
datos_excel = datos_excel.rename(columns={"PAY_0": "PAY_1"})

# Convertir todas las columnas a tipos de datos numéricos
datos_excel = datos_excel.apply(pd.to_numeric, errors='coerce')
