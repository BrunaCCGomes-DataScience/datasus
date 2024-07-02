# Configuração e Execução

## Criar o ambiente virtual

### 1. Navegar até o diretório onde deseja criar o ambiente virtual:
*sh*
```
cd D:\GitHub\datasus\datasus-data-integration\dir-col-match
```
### 2. Criar o ambiente virtual:
*sh*
```
python -m venv venv
```
### 3. Ativar o ambiente virtual:
*sh*
```
.\venv\Scripts\Activate.ps1
```

## Instalar dependências
*sh*
```
pip install -r requirements.txt
```

## Executar a aplicação
*sh*
```
python src/main.py
```

*bash*

#### 1.2. `.gitignore`

```plaintext
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
env/
venv/
ENV/
env.bak/
venv.bak/
```

##### Config files
```
*.env
```

##### IDEs
```
.vscode/
.idea/
```

##### OS files
```
.DS_Store
Thumbs.db
```

#### 1.3. `requirements.txt`
```
Django==4.2
psycopg2-binary==2.9.3
pymssql==2.2.2
```