#!/usr/bin/env python

import sys
import json
import logging
import csv
import shutil

default_parts = {'part': [{'synbiohub': 'https://synbiohub.org/public/igem/BBa_K1847014/1', 'type': 'promoter', 'name': 'PlacUV5'}, {'synbiohub': 'https://synbiohub.org/public/igem/BBa_J56012/1', 'type': 'promoter', 'name': 'Ptrc'}, {'synbiohub': 'https://synbiohub.org/public/igem/BBa_I50041/1', 'type': 'origin', 'name': 'BBR1'}, {'synbiohub': 'https://synbiohub.org/public/igem/BBa_I50032/1', 'type': 'origin', 'name': 'p15A'}, {'synbiohub': 'https://synbiohub.org/public/igem/BBa_J64101/1', 'type': 'origin', 'name': 'ColE1'}, {'synbiohub': 'https://synbiohub.org/public/igem/BBa_I13800/1', 'type': 'resistance', 'name': 'res1'}, {'synbiohub': 'https://synbiohub.org/public/igem/BBa_B1006/1', 'type': 'terminator', 'name': 'Ter'}]}

if __name__ == "__main__":
    input_json_path = sys.argv[1]
    logging.info(input_json_path)
    output_path = sys.argv[2]
    logging.info(output_path)
    with open(input_json_path, 'r') as f:
        try:
            input_dict = json.load(f)
        except json.decoder.JSONDecodeError:
            input_dict = {}
        logging.info(input_dict)
    #when the input is empty revert to the defaukt
    if not input_dict or input_dict=={'part': []}:
        logging.warning('Empty of error reading the parts... reverting to the default')
        input_dict = default_parts
    #if the input is not empty
    with open(output_path, 'w') as infi:
        csvfi = csv.writer(infi, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvfi.writerow(['Name', 'Type', 'Part'])
        for part in input_dict['part']:
            csvfi.writerow([part['name'], part['type'], part['synbiohub']])
