# src/utils/config.py
import os

class Config:
    def __init__(self):
        self.input_dir = os.getenv('INPUT_DIR', 'data/input')
        self.output_dir = os.getenv('OUTPUT_DIR', 'data/output')
