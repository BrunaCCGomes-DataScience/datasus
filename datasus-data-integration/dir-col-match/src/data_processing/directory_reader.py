# data_integration/data_processing/directory_reader.py

import os
from utils.config import Config

class DirectoryReader:
    def __init__(self):
        self.config = Config()

    # Se include for True, ele inclui apenas os arquivos 
    # que começam com algum dos prefixos da lista SIGLA_UF. 
    # Se include for False, ele inclui apenas os arquivos 
    # que não começam com nenhum dos prefixos da lista SIGLA_UF.
    def filter_files_by_prefixes(self, include=True):
        filtered_files = []
        prefixes = self.config.SIGLA_UF

        for file in os.listdir(self.config.directory_files_compare_path):
            file_name = file.lower()

            if include:
                if any(file_name.startswith(prefix) for prefix in prefixes):
                    filtered_files.append(file)
            else:
                if not any(file_name.startswith(prefix) for prefix in prefixes):
                    filtered_files.append(file)

        return filtered_files

    # Se include for True, ele inclui apenas os arquivos que 
    # começam com o specific_prefix. 
    # Se include for False, ele inclui apenas os arquivos 
    # que não começam com o specific_prefix.
    def filter_files_by_specific_prefix(self, specific_prefix, include=True):
        filtered_files = []

        for file in os.listdir(self.config.directory_files_compare_path):
            file_name = file.lower()

            if include:
                if file_name.startswith(specific_prefix):
                    filtered_files.append(file)
            else:
                if not file_name.startswith(specific_prefix):
                    filtered_files.append(file)

        return filtered_files
