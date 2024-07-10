import os
import sys
import csv
from dbfread import DBF
from utils.config import Config

class DBCProcessor:
    def __init__(self, dataframes):
        self.config = Config()
        self.dataframes = dataframes
        
    # def process_file(self):
    #     file_path = os.path.join(self.config.input_dir, "filename")
    #     print(file_path)
    #     table = DBF('files/people.dbf')
    #     writer = csv.writer(sys.stdout)

    #     writer.writerow(table.field_names)
    #     for record in table:
    #         writer.writerow(list(record.values()))
        

    def process(self):
        processed_data = []
        for df in self.dataframes:
            # Implementar o processamento específico dos dados aqui
            # Por exemplo, limpar, transformar, filtrar, etc.
            processed_data.append(df)
        return processed_data
