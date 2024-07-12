import os
import shutil

# Variável para rastrear se alguma pasta __pycache__ foi encontrada
found_pycache = False

for root, dirs, files in os.walk('.'):
    for dir in dirs:
        if dir == '__pycache__':
            dir_path = os.path.join(root, dir)
            print(f"Removing {dir_path}")
            shutil.rmtree(dir_path)
            found_pycache = True

if found_pycache:
    print("Processo concluído: Todas as pastas '__pycache__' foram removidas.")
else:
    print("Nenhuma pasta '__pycache__' foi encontrada.")
