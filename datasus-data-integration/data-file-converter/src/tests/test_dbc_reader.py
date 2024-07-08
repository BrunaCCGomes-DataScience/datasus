import unittest
from data_processing.dbc.dbc_reader import DBCReader
import os

class TestDBCReader(unittest.TestCase):
    def setUp(self):
        self.input_dir = 'data/input'
        os.makedirs(self.input_dir, exist_ok=True)
        # Criar arquivos de teste .dbc aqui, se necessário

    def tearDown(self):
        # Remover arquivos de teste .dbc aqui, se necessário
        pass

    def test_read_files(self):
        reader = DBCReader(self.input_dir)
        dataframes = reader.read_files()
        self.assertIsInstance(dataframes, list)

if __name__ == "__main__":
    unittest.main()
