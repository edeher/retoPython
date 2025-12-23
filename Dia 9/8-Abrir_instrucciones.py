import shutil
from pathlib import Path

dest = Path(r"C:\Users\yosoy\Documentos\Projetcs Python\project1\Dia 9")
shutil.unpack_archive('ProyectoDia9.zip', str(dest), 'zip')
