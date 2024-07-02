import unittest
from src.data_processing.file_copier import FileCopier
import os

class TestFileCopier(unittest.TestCase):
    def setUp(self):
        self.source_path = 'test_data/source/'
        self.destination_path = 'test_data/destination/'
        os.makedirs(self.source_path, exist_ok=True)
        with open(os.path.join(self.source_path, 'file_to_copy.txt'), 'w') as file:
            file.write('dummy content')

    def tearDown(self):
        for file_name in os.listdir(self.source_path):
            os.remove(os.path.join(self.source_path, file_name))
        os.rmdir(self.source_path)
        for file_name in os.listdir(self.destination_path):
            os.remove(os.path.join(self.destination_path, file_name))
        os.rmdir(self.destination_path)

    def test_copy_files(self):
        file_paths = [os.path.join(self.source_path, 'file_to_copy.txt')]
        file_copier = FileCopier(self.destination_path)
        file_copier.copy_files(file_paths)
        self.assertTrue(os.path.exists(os.path.join(self.destination_path, 'file_to_copy.txt')))

if __name__ == '__main__':
    unittest.main()
