import argparse

from converter import convert_csv_to_json


def main():
    parser = argparse.ArgumentParser(description="Convert a CSV file to a JSON file.")

    parser.add_argument("input_file", type=str, help="Path to the input CSV file")

    parser.add_argument("output_file", type=str, help="Path to the output JSON file.")

    args = parser.parse_args()
    convert_csv_to_json(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
