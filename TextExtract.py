import nltk
import os
import re
import pytesseract
import tqdm
import matplotlib.pyplot as plt 
from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path

def textExtract(filename, out_file='out.txt'):
    
    PDF_file = Path(filename)
    pdf_pages = convert_from_path(PDF_file, dpi=200)

    text = "\n"

    for page in tqdm.tqdm(pdf_pages):
        
        custom_oem_psm_config = r'--oem 1'

        text += pytesseract.image_to_string(page, config=custom_oem_psm_config) 
        
        text = re.sub(r'\$\w*', '', text)
        text = re.sub(r'^RT[\s]+', '', text)
        text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
        text = re.sub(r'#', '', text)

        text += "\nNEXT PAGE\n"
    
    return text

print(textExtract('./TestNASA/19740076600.pdf'))
    
    