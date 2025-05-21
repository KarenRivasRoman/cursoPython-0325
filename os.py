import os

#obtener el directorio actual
"""cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)"""

#listar los archivos
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)

#renombrar
os.rename('cuento.txt', 'caperucita.txt')
print('Archivo renombrado')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)

