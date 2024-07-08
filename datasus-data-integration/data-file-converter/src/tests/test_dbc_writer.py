import unittest
from data_processing.dbc.dbc_writer import DBCWriter
import pandas as pd
import os

class TestDBCWriter(unittest.TestCase):
    def setUp(self):
        self.output_dir = 'data/output'
        os.makedirs(self.output_dir, exist_ok=True)

    def tearDown(self):
        # Remover arquivos de saída criados durante os testes, se necessário
        pass

    def test_write_to_csv(self):
        writer = DBCWriter(self.output_dir)
        dataframes = [pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})]
        writer.write_to_csv(dataframes)
        output_files = os.listdir(self.output_dir)
        self.assertTrue(len(output_files) > 0)

if __name__ == "__main__":
    unittest.main()
