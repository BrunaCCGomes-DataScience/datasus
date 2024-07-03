# data_integration/utils/config.py

import os

SIGLA_UF = [
    'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms',
    'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc',
    'sp', 'se', 'to'
]

class Config:
    def __init__(self):
        self.dataset_path = os.getenv('DATASET_PATH', 'data/input/dataset.csv')
        self.directory_path = os.getenv('DIRECTORY_PATH', 'data/input/')
        self.destination_path = os.getenv('DESTINATION_PATH', 'data/output/')
        self.column_separator = os.getenv('COLUMN_SEPARATOR', ',')
        self.sigla_uf = os.getenv('SIGLA_UF', 'sp').lower()