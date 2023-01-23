#!/usr/bin/env python
import sys
import os
from multiprocessing.dummy import Pool
import re



def main():
    start_folder = sys.argv[1]
    file_paths = []
    for curr_dir, dir_list, file_list in os.walk(start_folder):
        for file_name in file_list:
            file_paths.append(os.path.join(curr_dir, file_name))

    pool = Pool(64)
    results = pool.map(analyze_file, file_paths)
    total_files = len(file_paths)
    total_bytes = sum(r[0] for r in results)
    total_lines = sum(r[1] for r in results)
    print("Number of files:", total_files)
    print("Number of bytes:", total_bytes)
    print("Number of lines:", total_lines)



def analyze_file(file_path):
    with open(file_path, "rb") as file_in:
        contents = file_in.read()
        num_bytes = len(contents)
        num_lines = contents.count(b'\n')
        return num_bytes, num_lines

if __name__ == '__main__':
    main()
