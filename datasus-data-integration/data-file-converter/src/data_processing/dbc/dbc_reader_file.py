from dbfread import DBF
import os
import encodings.cp1252
from pandas import DataFrame
from utils.config import Config
import unicodedata
import sys
import csv
import codecs
import encodings 
#from codecs import Codec
# from encodings.cp1252 import Codec


class DBCReaderFile:
    def __init__(self, input_dir):
        self.config = Config()
        #self.codec = Codec()    

    def read_files_codec(self,str_to_decode):
        # byte string to be converted
        # str_to_decode = b'\xc3\xa9\xc3\xa0\xc3\xb4'
        codecs.getencoder('CP_ACP')
        print(str_to_decode)
        
        # decoding the byte string to unicode string
        CP_ACP_string = codecs.decode(str_to_decode, 'CP_ACP')
        print(CP_ACP_string)
        CP_OEMCP_string = codecs.decode(str_to_decode, 'CP_OEMCP')        
        print(CP_OEMCP_string)


    def read_files(self):
        dbc_data = []
        for filename in os.listdir(self.config.input_dir):
            if filename.endswith(".dbc"):            
                file_path = os.path.join(self.config.input_dir, filename)
                print(file_path)

                tblDBF = DBF(file_path,  char_decode_errors='ignore', raw=True, load=True,  ignore_missing_memofile=True)                 
                # tblDBF = DBF(file_path, encoding='CP_ACP', char_decode_errors='strict', raw=True, load=False,  ignore_missing_memofile=True)  
                # tblDBF = DBF(file_path, char_decode_errors='ignore', raw=True, load=False,  ignore_missing_memofile=True)  
                print(tblDBF.encoding)                              
                     
                lstRecord = []       
                ct = 0  
                
                tblDBF.load()    
                for chave, valor in tblDBF.records[0].items():  
                    if ct <= 25:
                        print(f"Chave: {chave}, Valor: {valor}") 
                        str_original = valor
                        unicodedata.normalize(str_original)
                        # bytes_encoded = str_original.decode(encoding='ascii')
                        # print(type(bytes_encoded))
                       
                        #valorxpto = str_original.codecs.BOM_UTF8.decode()
                        
                        # b_string = valor
                        # print(b_string)
                        # jj = str(b_string)
                        # print(jj)

                        # encodings.normalize_encoding(encoding='ascii') 
                        # encodings._alias_mbcs('CP_ACP')

                        # str_decoded = bytes_encoded.decode()
                        # print(type(str_decoded))                       
                        # codecs.oem_decode
                        xpto = codecs.Codec.encode('CP_ACP', str_original, errors='ignore')
                        print(xpto)
                        n1_valor = str_original.decode('CP_ACP')
                        print(f"Chave: {chave}, Valor: {n1_valor}")
                        
                        n2_valor = str_original.decode('CP_OEMCP')
                        print(f"Chave: {chave}, Valor: {n2_valor}")

                        # lstRecord.append(tblDBF.records[0].items())
                        lstRecord.append(valor)
                        ct += 1
                    else:
                        break                           
                dbc_data.append(lstRecord)
                tblDBF.unload()
        return dbc_data         