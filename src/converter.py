import csv
import json


def convert_csv_to_json(input_file, output_file, delimiter=","):
    try:
        with open(input_file, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            data = list(reader)
        with open(output_file, mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2)

        print(f" Successfully converted '{input_file}' to '{output_file}'")

    except FileNotFoundError:
        print(f" Error: The file {input_file} was not found.")

    except Exception as e:
        print(f"An Error occurred {e}")
