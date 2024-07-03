#### Arquitetura do Sistema Back-End

## Visão da Estrutura de Diretórios

A estrutura de diretórios para o projeto deve ser organizada da seguinte forma:

```plaintext
datasus-data-integration/
│   └── data-file-converter/
│   	└── data/
│   	│   ├── input/
│   	│   ├── output/
│   	│   └── reference/
│		└── src/
│   	│	├── main.py
│   	│	├── data_processing/
│   	│	│   ├── __init__.py
│   	│	│   ├── dbc/
│   	│	│   │   ├── __init__.py
│   	│	│   │   ├── dbc_reader.py
│   	│	│   │   ├── dbc_processor.py
│   	│	│   │   └── dbc_writer.py
│   	│	│   ├── csv/
│   	│	│   │   ├── __init__.py
│   	│	│   │   ├── csv_reader.py
│   	│	│   │   ├── csv_processor.py
│   	│	│   │   └── csv_writer.py
│   	│	│   ├── txt/
│   	│	│   │   ├── __init__.py
│   	│	│   │   ├── txt_reader.py
│   	│	│   │   ├── txt_processor.py
│   	│	│   │   └── txt_writer.py
│   	│	│   ├── dbf/
│   	│	│   │   ├── __init__.py
│   	│	│   │   ├── dbf_reader.py
│   	│	│   │   ├── dbf_processor.py
│   	│	│   │   └── dbf_writer.py
│   	│	│   ├── dat/
│   	│	│   │   ├── __init__.py
│   	│	│   │   ├── dat_reader.py
│   	│	│   │   ├── dat_processor.py
│   	│	│   │   └── dat_writer.py
│   	│	│   ├── xls/
│   	│	│   │   ├── __init__.py
│   	│	│   │   ├── xls_reader.py
│   	│	│   │   ├── xls_processor.py
│   	│	│   │   └── xls_writer.py
│   	│	│   ├── xml/
│   	│	│   │   ├── __init__.py
│   	│	│   │   ├── xml_reader.py
│   	│	│   │   ├── xml_processor.py
│   	│	│   │   └── xml_writer.py
│   	│	│   ├── json/
│   	│	│   │   ├── __init__.py
│   	│	│   │   ├── json_reader.py
│   	│	│   │   ├── json_processor.py
│   	│	│   │   └── json_writer.py
│   	│	│   └── __init__.py
│   	│	├── utils/
│   	│	│   ├── __init__.py
│   	│	│   ├── logger.py
│   	│	│   └── config.py
│   	│	└── tests/
│   	│	    ├── __init__.py
│   	│	    ├── test_dbc_reader.py
│   	│	    ├── test_dbc_processor.py
│   	│	    ├── test_csv_reader.py
│   	│	    ├── test_csv_processor.py
│   	│	    ├── test_txt_reader.py
│   	│	    ├── test_txt_processor.py
│   	│	    ├── test_dbf_reader.py
│   	│	    ├── test_dbf_processor.py
│   	│	    ├── test_dat_reader.py
│   	│	    ├── test_dat_processor.py
│   	│	    ├── test_xls_reader.py
│   	│	    ├── test_xls_processor.py
│   	│	    ├── test_xml_reader.py
│   	│	    ├── test_xml_processor.py
│   	│	    ├── test_json_reader.py
│   	│	    └── test_json_processor.py
		
```
## Criando Estrutura de Diretórios no VS Code
- **Diretório Principal:** D:\GitHub\datasus\datasus-data-integration\data-file-converter
- Via Terminal PorwerShell

### 1. Criar o ambiente virtual :
- #### Navegar até o diretório onde deseja criar o ambiente virtual
  *PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>* ```cd D:\GitHub\datasus\datasus-data-integration\data-file-converter```
- #### Criar o ambiente virtual
  *PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>* ```python -m venv venv```

### 2. Ativar o ambiente virtual:
- #### Ativar o ambiente virtual no Windows
  *PS D:\GitHub\datasus\datasus-data-integration\data-file-converter>* ```.\venv\Scripts\Activate.ps1```

### 3. Criar a estrutura de diretórios e arquivos do projeto:
- #### Criar diretórios
```
mkdir data
mkdir data\input
mkdir data\output
mkdir data\reference

mkdir src
mkdir src\data_processing
mkdir src\data_processing\dbc
mkdir src\data_processing\csv
mkdir src\data_processing\txt
mkdir src\data_processing\dbf
mkdir src\data_processing\dat
mkdir src\data_processing\xls
mkdir src\data_processing\xml
mkdir src\data_processing\json

mkdir src\utils
mkdir src\tests

```
- #### Criar os arquivos .gitkeep dentro dos diretórios
New-Item -Path data\input\.gitkeep -ItemType File
New-Item -Path data\output\.gitkeep -ItemType File
New-Item -Path data\reference\.gitkeep -ItemType File
```

- #### Criar arquivos dentro de src
```
New-Item -ItemType file .\src\main.py
New-Item -ItemType file .\src\data_processing\__init__.py

New-Item -ItemType file .\src\data_processing\dbc\__init__.py
New-Item -ItemType file .\src\data_processing\dbc\dbc_reader.py
New-Item -ItemType file .\src\data_processing\dbc\dbc_processor.py
New-Item -ItemType file .\src\data_processing\dbc\dbc_writer.py

New-Item -ItemType file .\src\data_processing\csv\__init__.py
New-Item -ItemType file .\src\data_processing\csv\csv_reader.py
New-Item -ItemType file .\src\data_processing\csv\csv_processor.py
New-Item -ItemType file .\src\data_processing\csv\csv_writer.py

New-Item -ItemType file .\src\data_processing\txt\__init__.py
New-Item -ItemType file .\src\data_processing\txt\txt_reader.py
New-Item -ItemType file .\src\data_processing\txt\txt_processor.py
New-Item -ItemType file .\src\data_processing\txt\txt_writer.py

New-Item -ItemType file .\src\data_processing\dbf\__init__.py
New-Item -ItemType file .\src\data_processing\dbf\dbf_reader.py
New-Item -ItemType file .\src\data_processing\dbf\dbf_processor.py
New-Item -ItemType file .\src\data_processing\dbf\dbf_writer.py

New-Item -ItemType file .\src\data_processing\dat\__init__.py
New-Item -ItemType file .\src\data_processing\dat\dat_reader.py
New-Item -ItemType file .\src\data_processing\dat\dat_processor.py
New-Item -ItemType file .\src\data_processing\dat\dat_writer.py

New-Item -ItemType file .\src\data_processing\xls\__init__.py
New-Item -ItemType file .\src\data_processing\xls\xls_reader.py
New-Item -ItemType file .\src\data_processing\xls\xls_processor.py
New-Item -ItemType file .\src\data_processing\xls\xls_writer.py

New-Item -ItemType file .\src\data_processing\xml\__init__.py
New-Item -ItemType file .\src\data_processing\xml\xml_reader.py
New-Item -ItemType file .\src\data_processing\xml\xml_processor.py
New-Item -ItemType file .\src\data_processing\xml\xml_writer.py

New-Item -ItemType file .\src\data_processing\json\__init__.py
New-Item -ItemType file .\src\data_processing\json\json_reader.py
New-Item -ItemType file .\src\data_processing\json\json_processor.py
New-Item -ItemType file .\src\data_processing\json\json_writer.py

New-Item -ItemType file .\src\utils\__init__.py
New-Item -ItemType file .\src\utils\logger.py
New-Item -ItemType file .\src\utils\config.py
```

- #### Criar arquivos dentro de tests
```
New-Item -ItemType file .\src\tests\__init__.py
New-Item -ItemType file .\src\tests\test_dbc_reader.py
New-Item -ItemType file .\src\tests\test_dbc_processor.py
New-Item -ItemType file .\src\tests\test_csv_reader.py
New-Item -ItemType file .\src\tests\test_csv_processor.py
New-Item -ItemType file .\src\tests\test_txt_reader.py
New-Item -ItemType file .\src\tests\test_txt_processor.py
New-Item -ItemType file .\src\tests\test_dbf_reader.py
New-Item -ItemType file .\src\tests\test_dbf_processor.py
New-Item -ItemType file .\src\tests\test_dat_reader.py
New-Item -ItemType file .\src\tests\test_dat_processor.py
New-Item -ItemType file .\src\tests\test_xls_reader.py
New-Item -ItemType file .\src\tests\test_xls_processor.py
New-Item -ItemType file .\src\tests\test_xml_reader.py
New-Item -ItemType file .\src\tests\test_xml_processor.py
New-Item -ItemType file .\src\tests\test_json_reader.py
New-Item -ItemType file .\src\tests\test_json_processor.py

```
- #### Criar arquivos adicionais
```
New-Item -ItemType file .\requirements.txt
New-Item -ItemType file .\README.md
New-Item -ItemType file .\configuracao-execucao.md
New-Item -ItemType file .\implementacao.md
New-Item -ItemType file .\.gitignore

```