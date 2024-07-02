import os
import shutil

class FileCopier:
    def __init__(self, destination_path):
        self.destination_path = destination_path

    def copy_files(self, file_paths):
        if not os.path.exists(self.destination_path):
            os.makedirs(self.destination_path)

        for file_path in file_paths:
            shutil.copy(file_path, self.destination_path)
