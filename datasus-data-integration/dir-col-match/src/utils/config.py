import os

class Config:
    def __init__(self):
        self.dataset_path = os.getenv('DATASET_PATH', 'data/input/dataset.csv')
        self.directory_path = os.getenv('DIRECTORY_PATH', 'data/input/')
        self.destination_path = os.getenv('DESTINATION_PATH', 'data/output/')
        self.column_separator = os.getenv('COLUMN_SEPARATOR', ',')
