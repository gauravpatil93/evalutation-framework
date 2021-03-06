#!/usr/bin/python3
#author Colin Etzel
import argparse
from trec_car.read_data import *

parser = argparse.ArgumentParser()
parser.add_argument("outline_file", type=str, help="Qualified location of the outline file")
parser.add_argument("output_file", type=str, help="Name of the output file")
args = vars(parser.parse_args())

query_cbor = args['outline_file']
output_file_name = args['output_file']

pages = []
with open(query_cbor, 'rb') as f:
    for p in itertools.islice(iter_annotations(f), 0, 1000):
        pages.append(p)

# Generate queries in plain text
plain_text_queries = []
for page in pages:
    for section_path in page.flat_headings_list():
        query_id_plain = " ".join([page.page_name] + [section.heading for section in section_path])
        query_id_formatted = "/".join([page.page_id] + [section.headingId for section in section_path])
        tup = (query_id_plain, query_id_formatted)
        plain_text_queries.append(tup)

outfile = open(str(output_file_name), "w")
for tup in plain_text_queries:
    outfile.write(tup[0]+"\n")
    outfile.write(tup[1]+"\n")