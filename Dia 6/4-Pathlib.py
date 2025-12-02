from pathlib import Path, PureWindowsPath
carpeta = Path('C:/Users/yosoy/OneDrive/Documentos/Projetcs Python/project1/'
               'files/otro_file.txt')
print(carpeta.read_text())
print('-----------------')
print(carpeta.name)
print('-----------------')
print(carpeta.suffix)
print('-----------------')
print(carpeta.stem)
print('-----------------')
print(carpeta.exists())
print('-----------------')

ruta_windows = PureWindowsPath(carpeta)
print('ruta windows : ', ruta_windows)