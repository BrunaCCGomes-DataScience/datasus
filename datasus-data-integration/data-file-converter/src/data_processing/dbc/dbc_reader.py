from dbfread import DBF
import os
from pandas import DataFrame
from utils.config import Config
import unicodedata
import sys
import csv
import codecs

class DBCReader:
    def __init__(self, input_dir):
        self.config = Config()

    # Função para normalizar strings
    def normalize_string(s):
        print(unicodedata.normalize('NFC', s).encode('ascii', 'ignore').decode('ascii'))
        print(unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('ascii'))

        # print(unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii'))        
        # print(unicodedata.normalize('NFKC', s).encode('ascii', 'ignore').decode('ascii'))
        # print(unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii'))
        return unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('ascii')

    # Caminho para o arquivo DBF
    #dbf_path = 'caminho/para/sua/tabela.dbf'

    # Leitura da tabela DBF
    # table = DBF(dbf_path, load=True)

    # # Iteração sobre os registros e normalização das strings
    # for record in table:
    #     normalized_record = {k: normalize_string(v) if isinstance(v, str) else v for k, v in record.items()}
    #     print(normalized_record)


    # Escreve arquivo .csv a partir do .DBF
    # Verifica estrutura de diretório e arquivo
    def write_file_csv(self, table_csv):
        path_output_dir = self.config.output_dir
        os.makedirs(path_output_dir, exist_ok=True)
        file_path_output_dir = os.path.join(path_output_dir, 'output.csv')
        
        # Escrita do arquivo CSV após verificação de diretório e arquivo
        with open(file_path_output_dir, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';',quoting=csv.QUOTE_NONE, escapechar='\\')            
            # normalize(table_csv)
            writer.writerow(table_csv.field_names)
            for record in table_csv:
                print(list(record.values()))     
                writer.writerow(list(record.values()))

        # Leitura do arquivo CSV após escrita
        with open(file_path_output_dir, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
            header = next(reader)  # Lê a linha de cabeçalho
            print("Cabeçalho:")
            print(header)
            
            print("Primeiras 10 linhas:")
            for _ in range(10):
                try:
                    row = next(reader)
                    print(row)
                except StopIteration:
                    break
    
    # Gera pandas DataFrame a partir do .DBF
    def write_pandas_df(self, table_df):
        # df = DBF(path_file_df)
        frame = DataFrame(iter(table_df))
        print(frame)

    def read_files(self):
        dbc_data = []
        for filename in os.listdir(self.config.input_dir):
            if filename.endswith(".dbc"):            
                file_path = os.path.join(self.config.input_dir, filename)
                print(file_path)
                ## tblDBF = DBF(file_path, char_decode_errors='replace', encoding='utf-8', load=True, raw=True, ignore_missing_memofile=False)
                ## print(tblDBF.encoding) # cp1252

                # Leitura da tabela DBF
                # tblDBF = DBF(file_path, load=True)
                # tblDBF = DBF(file_path, char_decode_errors='ignore', encoding='utf-8', load=True, raw=True, ignore_missing_memofile=False)
                # tblDBF = DBF(file_path, char_decode_errors='ignore',  load=True, raw=True, ignore_missing_memofile=False)
                # records_1 = [] 
                tblDBF = DBF(file_path, char_decode_errors='ignore',  load=True, raw=True, ignore_missing_memofile=False)
                records_1 = [] 
                
               # Iteração sobre os registros e normalização das strings
                for record in tblDBF:
                    normalize_rec = codecs.encode(record, 'cp1252', errors='stricts')
                    normalized_record = {k: self.normalize_string(v) if isinstance(v, str) else v for k, v in record.items()}
                    ct = 0
                    print(normalized_record)
                    records_1.append(normalized_record)
                    ct += 1
                    if ct == 25:
                        break   

                # self.write_file_csv(tblDBF)
                # self.write_pandas_df(tblDBF)
                # records_1 = [] 
                # ct = 0
                # for record in tblDBF.fields:
                #     print(record)
                #     records_1.append(record)
                #     ct += 1
                #     if ct == 100:
                #         break   
                #print(records_1)
                dbc_data.append(records_1)
        return dbc_data         