from dbfread import DBF
import os
from pandas import DataFrame
from utils.config import Config
import codecs
import unicodedata
import sys
import csv
import encodings.cp1252
import encodings 
from codecs import Codec
from encodings.cp1252 import Codec

class DBCReaderFile:
    def __init__(self, input_dir):
        self.config = Config()   

    """
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
        """

    def read_files(self):
        dbc_data = []
        for filename in os.listdir(self.config.input_dir):
            if filename.endswith(".dbc"):            
                file_path = os.path.join(self.config.input_dir, filename)
                print(file_path)
                
                tblDBF = DBF(file_path,ignore_missing_memofile=True, char_decode_errors='replace') 
                """
                # tblDBF = DBF(file_path,  char_decode_errors='ignore', raw=True, load=True,  ignore_missing_memofile=True)                 
                # tblDBF = DBF(file_path, encoding='CP_ACP', char_decode_errors='strict', raw=True, load=False,  ignore_missing_memofile=True)  
                # tblDBF = DBF(file_path, char_decode_errors='ignore', raw=True, load=False,  ignore_missing_memofile=True)  
                """
                print(tblDBF.encoding, tblDBF.char_decode_errors)                              
                # tblDBF.recfactory
                lstRecord_1 = []   
                lstRecord_2 = []    
                ct = 0                 

                tblDBF.load()    
                for chave, valor in tblDBF.records[0].items():  
                    if ct <= 25:
                        print(f"Chave: {chave}, Valor: {valor}") 

                        str_original_1 = valor
                        print(str_original_1)
                        decoded_string_1 = codecs.decode(str_original_1,'utf-8')
                        print(decoded_string_1)

                        str_original_2 = valor
                        print(str_original_2)
                        decoded_string_2 = codecs.decode(str_original_2,'latin-1')
                        print(decoded_string_2)

                        lstRecord_1.append(decoded_string_1)
                        lstRecord_2.append(decoded_string_2)
                        ct += 1

                        """
                        # encoded_string = codecs.encode(str_original,tblDBF.encoding)
                        # print(encoded_string)

                        # encoded_string = codecs.encode(str_original,'utf-8')
                        # print(encoded_string)

                        # decoded_string = codecs.decode(encoded_string,'utf-8')
                        # print(decoded_string)

                        

                        # encoded_string = codecs.encode(str_original,'utf-8')
                        # print(encoded_string)

                        # decoded_string = codecs.decode(encoded_string,'utf-8')
                        # print(decoded_string)
                        
                        

                        #unicodedata.normalize(str_original)
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
                        # xpto = codecs.Codec.encode('CP_ACP', str_original, errors='ignore')
                        # print(xpto)
                        # n1_valor = str_original.decode('CP_ACP')
                        # print(f"Chave: {chave}, Valor: {n1_valor}")
                        
                        # n2_valor = str_original.decode('CP_OEMCP')
                        # print(f"Chave: {chave}, Valor: {n2_valor}")

                        # lstRecord.append(tblDBF.records[0].items())
                        """
                    else:
                        break                           
                dbc_data.append(lstRecord_1)
                dbc_data.append(lstRecord_2)
                tblDBF.unload()
        return dbc_data         