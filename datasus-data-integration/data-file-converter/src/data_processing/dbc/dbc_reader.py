from dbfread import DBF
# import dbf
# from simpledbf import Dbf5
import os
# import pandas as pd
from pandas import DataFrame
# import dbf_reader
# import csv.csv_writer
from utils.config import Config
from unicodedata import normalize
import sys
import csv

class DBCReader:
    def __init__(self, input_dir):
        self.config = Config()

    # Escreve arquivo .csv a partir do .DBF
    # Verifica estrutura de diretório e arquivo
    def write_file_csv(self, table_csv):
        path_output_dir = self.config.output_dir
        os.makedirs(path_output_dir, exist_ok=True)
        file_path_output_dir = os.path.join(path_output_dir, 'output.csv')
        
        # Escrita do arquivo CSV após verificação de diretório e arquivo
        with open(file_path_output_dir, mode='w', newline='', encoding='cp1252') as file:
            writer = csv.writer(file, delimiter=';',quoting=csv.QUOTE_NONE, escapechar='\\')            
            writer.writerow(table_csv.field_names)
            for record in table_csv:
                writer.writerow(list(record.values()))

        # Leitura do arquivo CSV após escrita
        with open(file_path_output_dir, mode='r', newline='', encoding='cp1252') as file:
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
                tblDBF = DBF(file_path, char_decode_errors='ignore', raw=True, ignore_missing_memofile=True)
                print(tblDBF.encoding) # cp1252
                self.write_file_csv(tblDBF)
                self.write_pandas_df(tblDBF)
                records_1 = [] 
                ct = 0
                for record in tblDBF.fields:
                    print(record)
                    records_1.append(record)
                    ct += 1
                    if ct == 100:
                        break   
                dbc_data.append(tblDBF)
        return dbc_data         