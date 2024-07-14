# Limpar Pacotes Instalados Globalmente
#### Se você deseja limpar os pacotes instalados globalmente para evitar conflitos futuros, você pode desinstalá-los. Aqui está como:

## 1. Gerar uma Lista de Pacotes Instalados:
# >>> pip freeze > installed_packages.txt

## 2. Desinstalar Pacotes Globalmente:
#### Use COMANDO SHELL ou SCRIPT abaixo para desinstalar os pacotes listados.

# 2.1 COMANDO SHELL
    ## No Windows PowerShell:
    ##### Get-Content installed_packages.txt | ForEach-Object { $_.Split('==')[0] } | ForEach-Object { pip uninstall -y $_ }
    ## No Unix (Linux/macOS):
    ##### cat installed_packages.txt | awk -F'==' '{print $1}' | xargs pip uninstall -y

# 2.2 SCRIPT (uninstall_global_packages.py)

import subprocess

# Abrir o arquivo com pacotes instalados globalmente
with open('installed_packages.txt') as f:
    packages = f.read().splitlines()

# Desinstalar cada pacote listado
for package in packages:
    subprocess.call(['pip', 'uninstall', '-y', package.split('==')[0]])
