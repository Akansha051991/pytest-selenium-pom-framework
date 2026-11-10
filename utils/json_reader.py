import json
import os

class JsonReader:
    @staticmethod
    def read_json(file_name= "test_data.json"):
        """Read JSON test data file from the data directory"""
        file_path =os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', file_name))
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except Exception as e:
            raise FileNotFoundError(f"Could not find or read JSON file at {file_path}. Error: {e}")