import json
import os
import tempfile
import unittest

from src.converter import convert_csv_to_json


class TestConvertCSVToJson(unittest.TestCase):

    def test_convert_creates_correct_json(self):
        csv_content = "name,age\nAlice,30\nBob,25"
        with tempfile.NamedTemporaryFile(
            mode="w+", suffix=".csv", delete=False
        ) as csv_file:
            csv_file.write(csv_content)
            csv_file_path = csv_file.name

        with tempfile.NamedTemporaryFile(
            mode="r+", suffix=".json", delete=False
        ) as json_file:
            json_file_path = json_file.name

        try:
            success = convert_csv_to_json(csv_file_path, json_file_path)
            self.assertTrue(success)

            with open(json_file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.assertIsInstance(data, list)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["name"], "Alice")
            self.assertEqual(data[1]["age"], "25")

        finally:
            os.remove(csv_file_path)
            os.remove(json_file_path)

    def test_file_not_found(self):
        result = convert_csv_to_json("non_existent.csv", "out.json")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
