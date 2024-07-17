## Configuração e Execução

### Criar o ambiente virtual :
- #### Navegar até o diretório onde deseja criar o ambiente virtual
  *PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>* ```cd D:\GitHub\datasus\datasus-data-integration\data-file-converter```
- #### Criar o ambiente virtual
  *PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>* ```python -m venv venv```

### Ativar o ambiente virtual:
- #### Ativar o ambiente virtual no Windows
  *PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>*  ```.\venv\Scripts\Activate.ps1```

### Gerar arquivo com lista de Módulos de dependências
- #### Criação de arquivo "requirements.txt"
- #### Esse comando listará todas as dependências instaladas no ambiente virtual.
  *PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>* ```pip freeze > requirements.txt```

### Instalar dependências
- #### Instalação de Módulos listados
  *PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>* ```pip install -r requirements.txt```

### Executar a aplicação
*PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>* ```python src/main.py```
