# CSV to JSON Converter

This project is a Python script that allows you to easily and quickly convert CSV files to JSON from the command line.

---

## Features

- Converts CSV files to JSON.
- Supports different CSV delimiters.
- Basic error handling (file not found, generic errors).
- Outputs pretty-printed JSON with indentation.

---

## Requirements

- Python 3
- No external libraries needed (only standard modules).

---

## Usage

Run the script from the terminal:

```bash
python convert.py <path_to_csv> <path_to_json> [--delimiter ";"]

```

- <path_to_csv>: Path to the CSV file you want to convert.

- <path_to_json>: Path where the JSON file will be saved.

- [--delimiter ";"]: Optional. Specify the CSV delimiter (default is comma ,).

---

## Screenshots

![Screenshot ](.screenshots/csv_to_json.gif)
