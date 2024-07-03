from utils.logger import setup_logger
from data_processing.file_reader import FileReader
from data_processing.file_comparator import FileComparator
from data_processing.file_copier import FileCopier
from utils.config import Config

def main():
    # Setup logger
    logger = setup_logger()

    # Load configurations
    config = Config()

    # Read the dataset file
    file_reader = FileReader(config.dataset_path, config.column_separator)
    column_names = file_reader.get_column_names()

    # Compare column names with directory files
    file_comparator = FileComparator(config.directory_path, column_names)
    matched_files = file_comparator.find_matching_files()

    # Copy matched files to the destination directory
    file_copier = FileCopier(config.destination_path)
    file_copier.copy_files(matched_files)

    logger.info("Process completed successfully.")

if __name__ == "__main__":
    main()
