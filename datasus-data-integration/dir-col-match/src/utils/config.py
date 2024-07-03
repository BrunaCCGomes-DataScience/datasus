# data_integration/utils/config.py

import os

class Config:

    SIGLA_UF = [
    'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms',
    'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc',
    'sp', 'se', 'to'
]

    def __init__(self):
        self.directory_input_data_path = os.getenv('DIRECTORY_INPUT_DATA_PATH', 'data/input/')
        self.destination_path = os.getenv('DESTINATION_PATH', 'data/output/')
        self.destination_path_file_with_prefix = os.getenv('DESTINATION_PATH', 'data/output/uf/')
        self.destination_path_file_no_prefix = os.getenv('DESTINATION_PATH', 'data/output/no_uf/')
        self.column_separator = os.getenv('COLUMN_SEPARATOR', ';')
        self.sigla_uf = os.getenv('SIGLA_UF', 'sp').lower()
        self.dataset_file_compare_path = os.getenv('DATASET_FILE_COMPARE_PATH', 'data/input/dataset.csv')
        self.directory_files_compare_path = os.getenv('DIRECTORY_FILES_COMPARE_PATH', 'data/reference/CNV')