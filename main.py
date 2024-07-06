import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Konwerter plików .xml, .json, .yml")
    parser.add_argument("input_file", type=str, help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", type=str, help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")

import json

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    args = parse_args()
    data = read_json(args.input_file)
    print(data)
    
def write_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    args = parse_args()
    data = read_json(args.input_file)
    write_json(data, args.output_file)

