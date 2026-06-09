from pypdf import PdfReader, PdfWriter
import sys

inputs = sys.argv[1:] # grabs all args besides the first one which is just the Python file itself

def pdf_combiner(pdf_list):
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged.pdf')

pdf_combiner(inputs)