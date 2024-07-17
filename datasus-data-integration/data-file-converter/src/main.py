# import os
import pandas as pd
# from data_processing.dbc.dbc_reader import DBCReader
from data_processing.dbc.dbc_reader_file import DBCReaderFile
# from data_processing.dbc.dbc_processor import DBCProcessor
# from data_processing.dbc.dbc_writer import DBCWriter
from data_processing.dbc.dbc_detect_codec import DBCDetectCodec
from utils.config import Config
from utils.logger import setup_logger

config = Config()

def main():
    logger = setup_logger()
    logger.info("Iniciando verificação dos arquivos .dbc")

    logger.info("Detectando codecs dos arquivos .dbc")
    detector = DBCDetectCodec("")
    detector.detect_codec_files()
    
    # reader = DBCReaderFile(config.input_dir)
    # dataframes = reader.read_files()
    # print(dataframes.count)

    # logger.info("Processando os dados lidos")
    # processor = DBCProcessor(dataframes)
    # processed_data = processor.process()

    # logger.info("Escrevendo os dados processados em arquivos .csv")
    # writer = DBCWriter(config.output_dir)
    # writer.write_to_csv(processed_data)

    logger.info("Processamento concluído com sucesso")

if __name__ == "__main__":
    main()
