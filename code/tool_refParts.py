import sys
import json
import logging
import csv
import shutil

'''
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
)

logging.disable(logging.INFO)
logging.disable(logging.WARNING)
'''

if __name__ == "__main__":
    input_json_path = sys.argv[1]
    output_path = sys.argv[2]
    with open(input_json_path, 'r') as f:
        input_dict = json.load(f)
        logging.info(input_dict)
    #if the input is not empty
    if input_dict:
        logging.warning('Parsing the user parts')
        with open(output_path, 'w') as infi:
            csvfi = csv.writer(infi, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvfi.writerow(['Name', 'Type', 'Part'])
            for part in input_dict:
                csvfi.writerow([input_dict[part]['name'], input_dict[part]['type'], input_dict[part]['synbiohub']])
    #when the input is empty revert to the defaukt
    else:
        logging.warning('Passed empty input, sending default')
        shutil.copy('RefParts.csv', output_path)

