from dbfread import DBF
import os
from pandas import DataFrame
from utils.config import Config
import unicodedata
import sys
import csv
from codecs import Codec
# from encodings.cp1252 import Codec
import encodings 
# import encodings


class DBCReaderFile:
    def __init__(self, input_dir):
        self.config = Config()
        self.codec = Codec()    

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
                # tblDBF = DBF(file_path, char_decode_errors='ignore',  load=True, raw=True, ignore_missing_memofile=False)
                tblDBF = DBF(file_path, char_decode_errors='ignore', raw=True, ignore_missing_memofile=False)
                records_1 = [] 
                
               # Iteração sobre os registros e normalização das strings
                for record in tblDBF:
                    normalized_record = Codec.encode(record.items, 'cp1252', errors='ignore')
                    # normalized_record = {k: self.normalize_string(v) if isinstance(v, str) else v for k, v in record.items()}
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