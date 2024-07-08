import os
from data_processing.dbc.dbc_reader import DBCReader
from data_processing.dbc.dbc_processor import DBCProcessor
from data_processing.dbc.dbc_writer import DBCWriter
from utils.config import Config
from utils.logger import setup_logger

config = Config()

def main():
    logger = setup_logger()
    logger.info("Iniciando a leitura dos arquivos .dbc")

    reader = DBCReader(config.input_dir)
    dataframes = reader.read_files()

    logger.info("Processando os dados lidos")
    processor = DBCProcessor(dataframes)
    processed_data = processor.process()

    logger.info("Escrevendo os dados processados em arquivos .csv")
    writer = DBCWriter(config.output_dir)
    writer.write_to_csv(processed_data)

    logger.info("Processamento concluído com sucesso")

if __name__ == "__main__":
    main()
