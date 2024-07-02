import os

class FileComparator:
    def __init__(self, directory_path, column_names):
        self.directory_path = directory_path
        self.column_names = column_names

    def find_matching_files(self):
        matched_files = []
        for file_name in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, file_name)
            if os.path.isfile(file_path) and self._matches_columns(file_name):
                matched_files.append(file_path)
        return matched_files

    def _matches_columns(self, file_name):
        return any(column_name in file_name for column_name in self.column_names)
