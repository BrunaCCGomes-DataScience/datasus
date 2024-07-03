# data_integration/main.py

import os
from data_processing.directory_reader import DirectoryReader
from data_processing.file_reader import FileReader
from data_processing.file_comparator import FileComparator
from data_processing.file_copier import FileCopier
from utils.config import Config

config = Config()

def main():
    prefixed_files = False

    # Caso dataset para selecionar as colunas não exista, exibe msg.
    # Caso contrário, prossegue.
    if not os.path.exists(config.dataset_file_compare_path):
        print(f"File {config.dataset_file_compare_path} does not exist.")
        return

    file_reader = FileReader()
    column_names = file_reader.read_columns_from_dataset()

    # Caso diretório para seleção dos nomes dos arquivos para comprarar 
    # com o nome das colunas do dataset não exista, exibe msg.
    # Caso contrário, prossegue.
    if not os.path.exists(config.directory_files_compare_path):
        print(f"Directory {config.directory_files_compare_path} does not exist.")
        return
    
    directory_reader = DirectoryReader()
    file_comparator = FileComparator()
    file_copier = FileCopier()

    if(prefixed_files):
        # Return only files with prefixes in SIGLA_UF list.
        filtered_files_with_prefixes = directory_reader.filter_files_by_prefixes(include=True)
        print("Arquivos selecionados:", filtered_files_with_prefixes)
        
        # Compara o nome dos arquivos com o nome das colunas do dataset
        matching_files_with_prefixes = file_comparator.compare_column_names_with_files(column_names, filtered_files_with_prefixes, include=True)
      
        if(matching_files_with_prefixes):
            # Copia os arquvos que deram match para diretório indicado       
            file_copier.copy_matching_files(matching_files_with_prefixes,config.destination_path_file_with_prefix,prefix=True)
            print(f"Matching files with prefix copied to {config.destination_path_file_with_prefix}.")
  
    else:
        # Return only files without prefixes in SIGLA_UF list.
        filtered_files_no_prefixes = directory_reader.filter_files_by_prefixes(include=False)
        print("Arquivos selecionados:", filtered_files_no_prefixes)

        # Compara o nome dos arquivos com o nome das colunas do dataset
        matching_files_no_prefixes = file_comparator.compare_column_names_with_files(column_names, filtered_files_no_prefixes, include=False)

        if(matching_files_no_prefixes):
            # Copia os arquvos que deram match para diretório indicado
            file_copier.copy_matching_files(matching_files_no_prefixes,config.destination_path_file_no_prefix,prefix=False)
            print(f"Matching files no prefix copied to {config.destination_path_file_no_prefix}.")
    

if __name__ == "__main__":
    main()
