import unittest
from src.data_processing.file_comparator import FileComparator
import os

class TestFileComparator(unittest.TestCase):
    def setUp(self):
        self.directory_path = 'test_data/'
        self.column_names = ['col1', 'col2']
        os.makedirs(self.directory_path, exist_ok=True)
        with open(os.path.join(self.directory_path, 'file_with_col1.txt'), 'w') as file:
            file.write('dummy content')
        with open(os.path.join(self.directory_path, 'file_without_match.txt'), 'w') as file:
            file.write('dummy content')

    def tearDown(self):
        for file_name in os.listdir(self.directory_path):
            os.remove(os.path.join(self.directory_path, file_name))
        os.rmdir(self.directory_path)

    def test_find_matching_files(self):
        file_comparator = FileComparator(self.directory_path, self.column_names)
        matched_files = file_comparator.find_matching_files()
        self.assertEqual(len(matched_files), 1)
        self.assertTrue(any('file_with_col1.txt' in file for file in matched_files))

if __name__ == '__main__':
    unittest.main()
