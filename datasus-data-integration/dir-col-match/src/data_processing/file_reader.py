# data_integration/data_processing/file_reader.py

import csv
from utils.config import Config

class FileReader:
    def __init__(self):
        self.config = Config()

    def read_columns_from_dataset(self):
        with open(self.config.dataset_file_compare_path, 'r') as file:
            reader = csv.reader(file, delimiter=self.config.column_separator)
            columns = next(reader)
        return columns 