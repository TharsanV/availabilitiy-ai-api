import json

class JsonUtils:
    @staticmethod
    def load_json_from_file(filename):
        """Load JSON from a file and return it as a Python dictionary."""
        with open(filename, 'r') as file:
            return json.load(file)

    @staticmethod
    def assert_json_equal(actual, expected):
        """Compare two JSON objects (Python dictionaries) and assert they are equal."""
        assert actual == expected, f"JSON mismatch: \nExpected: {expected}\nActual: {actual}"