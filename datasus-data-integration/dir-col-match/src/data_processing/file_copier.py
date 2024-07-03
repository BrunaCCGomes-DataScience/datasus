# data_integration/data_processing/file_copier.py

import shutil
import os
from utils.config import Config

class FileCopier:
    def __init__(self):
        self.config = Config()

    def copy_matching_files(self, matching_files, destination_path_copy_files, prefix=True):
        if prefix:
            # Criar diretório  o prefixo da sigla do estado aos nomes das colunas
            if not os.path.exists(self.config.destination_path_file_with_prefix):
                os.makedirs(self.config.destination_path_file_with_prefix)
        else:
            if not os.path.exists(self.config.destination_path_file_no_prefix):
                os.makedirs(self.config.destination_path_file_no_prefix)

        for file in matching_files:
            source = os.path.join(self.config.directory_files_compare_path, file)
            destination = os.path.join(destination_path_copy_files, file)
            shutil.copyfile(source, destination)
