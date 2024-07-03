# data_integration/data_processing/file_comparator.py

from utils.config import Config

class FileComparator:
    def __init__(self):
        self.config = Config()

    def compare_column_names_with_files(self, column_names, files, include=False):
        matching_files = []
        prefix = f"{self.config.sigla_uf}_"

        for column in column_names:
            # new_column_name = (prefix + column).lower()
            for file in files:
                # Remove extensão do arquivo para comparação
                file_name = (file.split('.')[0]).lower()
                column_nm = column
                if "_" in column:
                    column_nm = (column.split('_')[1]).lower()
                if include:
                    # Adiciona o prefixo da sigla do estado aos nomes das colunas
                    # new_column_name = (prefix + column).lower()
                    new_column_name = (prefix + column_nm).lower()
                    if file_name == new_column_name:
                        matching_files.append(file)
                else:
                    if file_name == column_nm.lower():
                        matching_files.append(file)


                # # Adiciona o prefixo da sigla do estado aos nomes das colunas
                # if file_name == new_column_name:
                #     matching_files.append(file)
        return matching_files        
        
        # for column in column_names:
        #     new_column_name = (prefix + column).lower()
        #     for file in files:
        #         # Remove extensão do arquivo para comparação
        #         file_name = file.split('.')[0]
        #         # Adiciona o prefixo da sigla do estado aos nomes das colunas
        #         if file_name == prefix + column:
        #             matching_files.append(file)
        # return matching_files
