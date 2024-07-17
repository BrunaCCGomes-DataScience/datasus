import encodings.aliases
import encodings.charmap
from utils.config import Config
import os
import chardet
import encodings 
import codecs
import unicodedata
# from codecs import Codec

class DBCDetectCodec:
    def __init__(self, file_path):
        self.config = Config()  
        self.file_path = file_path  

    def detect_codec_files(self):
        dbc_data = []
        for filename in os.listdir(self.config.input_dir):
            if filename.endswith(".dbc"):            
                self.file_path = os.path.join(self.config.input_dir, filename)
                print(self.file_path) 
                # self.display_encoding()
                self.display_decoding()        
        return dbc_data         

    def detect_encoding(self):
        """Detecta a codificação do arquivo e retorna a codificação e a confiança."""
        with open(self.file_path, 'rb') as file:
            raw_data = file.read()

            print(encodings.search_function('utf-8').name)

            result1 = chardet.detect_all(raw_data)
            encoding1 = result1['encoding']
            confidence1 = result1['confidence']
            # return decoded_data
            # result = chardet.detect(raw_data)
            # encoding = result['encoding']
            # confidence = result['confidence']
        return encoding1, confidence1

    def display_encoding(self):
        """Exibe a codificação detectada e a confiança."""
        encoding, confidence = self.detect_encoding()
        print(f"Codificação detectada: {encoding} com confiança de {confidence:.2f}")

    def detect_and_decode(self):
        """Detecta a codificação do arquivo, retorna a codificação, a confiança e o conteúdo decodificado."""
        with open(self.file_path, 'rb') as file:
            raw_data = file.read()
            bytes.decode()
            bytes.decode(raw_data, encoding=str(codecs.BOM_UTF8),errors='ignore')
            bytes.decode(raw_data, encoding=str(codecs.utf_8_encode),errors='ignore')
            raw_data.decode(encoding=codecs.getdecoder('utf-8'))
            encodings.charmap.codecs.charmap_decode()
            bytes.decode()
            res = (chardet.detect(raw_data,should_rename_legacy=False))
            raw_data.decode(encoding='utf-8')
            
            encodings.search_function('utf-8')
            result1 = chardet.detect_all(raw_data)
            encoding1 = result1['encoding']
            confidence1 = result1['confidence']
            # result = chardet.detect(raw_data)
            # encoding = result['encoding']
            # confidence = result['confidence']
            decoded_content1 = raw_data.decode(encoding1) if encoding1 else None
        return encoding1, confidence1, decoded_content1

    def display_decoding(self):
        """Exibe a codificação detectada, a confiança e o conteúdo decodificado do arquivo."""
        encoding, confidence, decoded_content = self.detect_and_decode()
        print(f"Codificação detectada: {encoding} com confiança de {confidence:.2f}")
        if decoded_content:
            print("Conteúdo decodificado:")
            print(decoded_content)
        else:
            print("Não foi possível decodificar o conteúdo do arquivo.")

# def main():
#     file_path = 'seu_arquivo.dbc'
#     detector = DBCDetectCodec(file_path)
#     detector.display_encoding()
#     detector.display_decoding()

# if __name__ == "__main__":
#     main()
