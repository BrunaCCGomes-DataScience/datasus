#### Arquitetura do Sistema Back-End

## Visão da Estrutura de Diretórios

A estrutura de diretórios para o projeto deve ser organizada da seguinte forma:

```plaintext
project_root/                  >> Diretório raiz do projeto.
│
├── src/                       >> Contém todo o código-fonte do projeto.
│   ├── main.py                >> Arquivo principal que executa o fluxo da aplicação.
│   ├── data_processing/             >> Pacote com os módulos de processamento de dados.
│   │   ├── __init__.py                     >> 
│   │   ├── directory_reader.py             >> Módulo responsável pela seleção de arquivos.
│   │   ├── file_reader.py                  >> Módulo responsável pela leitura dos arquivos.
│   │   ├── file_comparator.py              >> Módulo responsável pela comparação dos arquivos.
│   │   └── file_copier.py                  >> Módulo responsável pela cópia dos arquivos.
│   ├── utils/                       >> Pacote com módulos utilitários.                   
│   │   ├── __init__.py                     >> 
│   │   ├── logger.py                       >> Módulo para configuração de logs.
│   │   ├── config.py                       >> Módulo para configuração do projeto.
│   └── tests/                       >> Pacote para os testes unitários.
│       ├── __init__.py                     >>
│       ├── test_directory_reader.py        >> Testes para o módulo de seleção de arquivos.
│       ├── test_file_reader.py             >> Testes para o módulo de leitura de arquivos.
│       ├── test_file_comparator.py         >> Testes para o módulo de comparação de arquivos.
│       └── test_file_copier.py             >> Testes para o módulo de cópia de arquivos.
│
├── data/                            >> Diretório para armazenar os dados utilizados e gerados pelo projeto.
│   ├── input/                          >> Contém os arquivos de entrada.
│   ├── output/                         >> Contém os arquivos de saída.
│   └── reference/                      >> Contém os arquivos de referência.
│
├── requirements.txt                        >> Lista de dependências do projeto.
├── README.md                               >> Arquivo de documentação do projeto.
└── .gitignore                              >> Arquivo para especificar quais arquivos/directórios devem ser ignorados pelo Git.
```

## Criar a estrutura de diretórios e arquivos do projeto:
- #### Criar diretórios
```
mkdir src
mkdir src/data_processing
mkdir src/utils
mkdir src/tests
mkdir data
mkdir data/input
mkdir data/output
mkdir data/output/no_uf
mkdir data/output/uf
mkdir data/reference
mkdir data/reference/CNV
```
- #### Criar os arquivos .gitkeep dentro dos diretórios
New-Item -Path data/input/.gitkeep -ItemType File
New-Item -Path data/output/no_uf/.gitkeep -ItemType File
New-Item -Path data/output/uf/.gitkeep -ItemType File
New-Item -Path data/reference/CNV/.gitkeep -ItemType File

- #### Criar arquivos dentro de src
```
New-Item -ItemType file .\src\main.py
New-Item -ItemType file .\src\data_processing\__init__.py
New-Item -ItemType file .\src\data_processing\directory_reader.py
New-Item -ItemType file .\src\data_processing\file_reader.py
New-Item -ItemType file .\src\data_processing\file_comparator.py
New-Item -ItemType file .\src\data_processing\file_copier.py
New-Item -ItemType file .\src\utils\__init__.py
New-Item -ItemType file .\src\utils\logger.py
New-Item -ItemType file .\src\utils\config.py
```
- #### Criar arquivos dentro de tests
```
New-Item -ItemType file .\src\tests\__init__.py
New-Item -ItemType file .\src\tests\test_directory_reader.py
New-Item -ItemType file .\src\tests\test_file_reader.py
New-Item -ItemType file .\src\tests\test_file_comparator.py
New-Item -ItemType file .\src\tests\test_file_copier.py
```
- #### Criar arquivos adicionais
```
New-Item -ItemType file .\requirements.txt
New-Item -ItemType file .\README.md
New-Item -ItemType file .\configuracao-execucao.md
New-Item -ItemType file .\implementacao.md
New-Item -ItemType file .\.gitignore
```