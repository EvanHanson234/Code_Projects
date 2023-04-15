# PDF Merger
# Combines all PDFs in the current directory into a single PDF
# To use this, make sure you activate the virtual environment and install PyPDF2
# Also make sure you have all the PDFs you want to combine in the same directory as this script

import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combined.pdf")