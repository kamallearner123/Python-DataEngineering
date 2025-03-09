#!/usr/bin/python3

import os
import sys
import json
import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)

def get_files_info(path):
    files_info = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_info = {
                'file_name': file,
                'file_path': file_path,
                'file_size': file_size
            }
            files_info.append(file_info)
    return files_info

def save_files_info(files_info, output_file):
    with open(output_file, 'w') as f:
        files_df = pd.DataFrame(files_info)
        files_df.to_csv(f, index=False)
    logging.info(f"Files info saved to {output_file}")
    
def main():
    if len(sys.argv) != 3:
        print("Usage: python CollectFilesInfo.py <path> <output_file>")
        sys.exit(1)
    
    path = sys.argv[1]
    output_file = sys.argv[2]
    
    logging.debug(f"Path: {path}")
    logging.debug(f"Output File: {output_file}")
    files_info = get_files_info(path)
    save_files_info(files_info, output_file)

if __name__ == '__main__':
    main()
