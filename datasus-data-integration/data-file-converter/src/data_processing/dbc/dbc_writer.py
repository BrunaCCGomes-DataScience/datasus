import os
from utils.config import Config

class DBCWriter:
    def __init__(self, output_dir):
        self.config = Config()

    def write_to_csv(self, dataframes):
        for i, df in enumerate(dataframes):
            output_path = os.path.join(self.config.output_dir, f"processed_data_{i}.csv")
            df.to_csv(output_path, index=False)
