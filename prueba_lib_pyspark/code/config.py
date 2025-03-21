import glob
from typing import Dict

import pandas as pd
from dataclasses import dataclass

BASE_PATH = "..\\files\\*.csv"
SAVE_FILES = "..\\saved_files"

@dataclass
class Table:
    name: str
    path: str
    df: pd.DataFrame


class DataReader:
    def __init__(self, base_path: str):
        """
        Initialize the DataReader class.
        :param base_path: The base path where files are located.
        """
        self.base_path: str = base_path
        self.table_dict: Dict[str, Table] = {}

    def read_all_files(self) -> None:
        """
        Reads all files from the base path and stores them as Table objects in a dictionary.
        Each Table object will contain the filename, the file path, and the DataFrame.
        """
        base_path_glob = glob.glob(self.base_path)

        for file in base_path_glob:
            name = file.split("\\")[-1]
            table = Table(name=name, path=file, df=pd.read_csv(file))
            self.table_dict[name] = table

        print(self.table_dict)
