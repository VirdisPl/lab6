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

import xml.etree.ElementTree as ET
import yaml

# Istniejące funkcje parse_args, read_json, write_json

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def write_xml(data, file_path):
    tree = ET.ElementTree(data)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

def write_yaml(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True)

def convert(input_file, output_file):
    input_ext = input_file.split('.')[-1]
    output_ext = output_file.split('.')[-1]

    if input_ext == 'json':
        data = read_json(input_file)
    elif input_ext == 'xml':
        data = read_xml(input_file)
    elif input_ext in ['yml', 'yaml']:
        data = read_yaml(input_file)
    else:
        raise ValueError("Nieobsługiwany format pliku wejściowego")

    if output_ext == 'json':
        write_json(data, output_file)
    elif output_ext == 'xml':
        write_xml(data, output_file)
    elif output_ext in ['yml', 'yaml']:
        write_yaml(data, output_file)
    else:
        raise ValueError("Nieobsługiwany format pliku wyjściowego")

if __name__ == "__main__":
    args = parse_args()
    convert(args.input_file, args.output_file)
