import unittest
from data_processing.dbc.dbc_processor import DBCProcessor
import pandas as pd

class TestDBCProcessor(unittest.TestCase):
    def test_process(self):
        dataframes = [pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})]
        processor = DBCProcessor(dataframes)
        processed_data = processor.process()
        self.assertIsInstance(processed_data, list)

if __name__ == "__main__":
    unittest.main()
