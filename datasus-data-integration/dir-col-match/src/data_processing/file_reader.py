import os

class FileReader:
    def __init__(self, file_path, separator):
        self.file_path = file_path
        self.separator = separator

    def get_column_names(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, 'r') as file:
            header = file.readline().strip()
            column_names = header.split(self.separator)
            return column_names
