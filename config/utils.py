import csv
import sys

#summarise the case details if required in case of overfow error 

def load_case(serial_no):
    with open('processed_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Serial No'] == str(serial_no):
                return row
    return None
