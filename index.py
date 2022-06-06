import openpyxl 
import numpy as np
import matplotlib.pyplot as plt

COLUMNAS = 7
FILAS_DATOS = 5
nombres = ['']
edades = []

# ------------ LEER ARCHIVO
workbook = openpyxl.load_workbook('data.xlsx')

# ------------ LEER HOJA 1
woorksheet = workbook.active

cells = woorksheet.iter_rows(min_row=2, max_col=COLUMNAS, max_row=FILAS_DATOS + 1, values_only=True)

# ------------ LEER CELDAS
for row in cells:
    nombres.append(f"{row[1]} {row[2]}")
    edades.append(int(row[6]))

# ------------ MOSTRAR GRÁFICA
fig, ax = plt.subplots()
ancho = 0.3
co = np.arange(FILAS_DATOS)

ax.bar(co, edades, ancho)
ax.set_title('Ventas Anuales')
ax.set_ylabel('Dolares')
ax.set_xlabel('Empleados')
ax.set_xticklabels(nombres)



