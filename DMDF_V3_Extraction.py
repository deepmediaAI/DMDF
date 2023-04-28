# extract_dmdf.py
from pathlib import Path
import os
import shutil


dataset_path = "dmdf_v2"
input_zips = []
input_zips += sorted(Path(dataset_path).glob('**/*.zip'))
input_zips = list(set(input_zips))
input_zips = [str(path) for path in input_zips]
input_zips = sorted(input_zips)

for input_zip in input_zips:
    unzip_directory = os.path.dirname(input_zip)
    shutil.unpack_archive(input_zip, unzip_directory)
    os.remove(input_zip)
    
#For Aligned Image Extraction

aligned_input_zips = []
aligned_input_zips += sorted(Path(dataset_path).glob('**/*/*.zip'))
aligned_input_zips = list(set(input_zips))
aligned_input_zips = [str(path) for path in input_zips]
aligned_input_zips = sorted(input_zips)

for input_zip in aligned_input_zips:
    unzip_directory = os.path.dirname(input_zip)
    shutil.unpack_archive(input_zip, unzip_directory)
    os.remove(input_zip)
