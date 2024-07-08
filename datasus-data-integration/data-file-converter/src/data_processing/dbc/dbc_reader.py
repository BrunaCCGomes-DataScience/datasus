from dbfread import DBF
import dbf
# from simpledbf import Dbf5
import os
import pandas as pd
# import dbf_reader
from utils.config import Config

class DBCReader:
    def __init__(self, input_dir):
        self.config = Config()

    def read_files(self):
        dbc_data = []
        for filename in os.listdir(self.config.input_dir):
            if filename.endswith(".dbc"):
                file_path = os.path.join(self.config.input_dir, filename)
                print(file_path)
                table = DBF(file_path)
                records = []
                ct = 0;
                for record in table.fields:
                    records.append(record)
                    ct += 1
                    if ct == 100:
                        break
                
                print(records)
                df = pd.DataFrame(records)
                # output_file_path = os.path.join(self.config.output_dir, filename)
                # dbf.export(table_or_records=records, filename='xxx', format='csv', header=True)
                # df_dbf = pd.DataFrame(records)
                # print(records)
                # table.close()
                    ## Or you can change it permanently (updates the DBF file) with:
                    ## table.open()
                    ## table.codepage = dbf.CodePage('cp1252') # for example
                    ## table.close()
                    ## dbfread
                    ##table = DBF(file_path)
                    ##records = [record for record in table]
                    ##df = pd.DataFrame(records)
                dbc_data.append(df)
        return dbc_data
    
    # def read_files(self):
    #     dbc_data = []
    #     for filename in os.listdir(self.config.input_dir):
    #         if filename.endswith(".dbc"):
    #             file_path = os.path.join(self.config.input_dir, filename)
    #             print(file_path)
    #             table = dbf.Table(filename=file_path, codepage=240)
    #             # dbf.export(file_path, filename=None, field_names=None, format='csv', header=True, dialect='dbf', encoding=None, ignore_errors=False, strip_nulls=False)
    #             # table = dbf.export(file_path, filename=None, field_names=None, format='csv', header=True, dialect='dbf', encoding=None, ignore_errors=False, strip_nulls=False)
    #             # table = dbf.export(file_path)
    #             table.open()
                
    #             # dbf.export(table_or_records=tb_dbf, filename='pa1', field_names=None, format='csv', header=True,)
    #             # dbf.export(table_or_records=tb_dbf, filename='PASP1', format='csv', header=True)
    #             # dbf.export()
    #             #df_dbf1 = pd.DataFrame(tb_dbf)
    #             # df_dbf1.head(3)
    #             # dbf.export(table_or_records=df_dbf1, filename='PASP1', format='csv', header=True)
    #             records = []
    #             ct = 0;
    #             for record in table.current_record:
    #                 records.append(record)
    #                 ct += 1
    #                 if ct == 100:
    #                     break
    #             # output_file_path = os.path.join(self.config.output_dir, filename)
    #             dbf.export(table_or_records=records, filename='xxx', format='csv', header=True)
    #             # df_dbf = pd.DataFrame(records)
    #             print(records)
    #             table.close()
    #                 ## Or you can change it permanently (updates the DBF file) with:
    #                 ## table.open()
    #                 ## table.codepage = dbf.CodePage('cp1252') # for example
    #                 ## table.close()
    #                 ## dbfread
    #                 ##table = DBF(file_path)
    #                 ##records = [record for record in table]
    #                 ##df = pd.DataFrame(records)
    #                 ##dbc_data.append(df)
    #     return dbc_data

