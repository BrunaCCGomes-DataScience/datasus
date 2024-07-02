import unittest
from src.data_processing.file_reader import FileReader
import os

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_data/test_dataset.csv'
        self.separator = ','
        with open(self.file_path, 'w') as file:
            file.write('col1,col2,col3\nvalue1,value2,value3\n')

    def tearDown(self):
        os.remove(self.file_path)

    def test_get_column_names(self):
        file_reader = FileReader(self.file_path, self.separator)
        column_names = file_reader.get_column_names()
        self.assertEqual(column_names, ['col1', 'col2', 'col3'])

if __name__ == '__main__':
    unittest.main()
