import json
import csv

def csv_to_json(csv_filepath, json_filepath):
    data  = []
    with open(csv_filepath, mode='r') as csvFile:
        csv_reader = csv.DictReader(csvFile)
        for row in csv_reader:
            data.append(row)
            print(row)

    with open(json_filepath, mode='w') as jsonFile:
        json.dump(data, jsonFile, indent=4)

csv_file_path = 'products_updated.csv'
json_file_path = 'output.json'
csv_to_json(csv_file_path, json_file_path)