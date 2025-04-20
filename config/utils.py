import csv
import sys

csv.field_size_limit(10**9)

def load_case(serial_no):
    with open('processed_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Serial No'] == str(serial_no):
                return row
    return None
