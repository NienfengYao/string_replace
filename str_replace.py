#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import argparse

def replace_text_in_files(folder_path, search_text, replace_text, exclude_dirs=None):
    modified_files = []  # 用來存放被修改的檔案名稱
    for root, dirs, files in os.walk(folder_path):
        if exclude_dirs:
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print("file_path:", file_path)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                if search_text in file_content:
                    modified_files.append(file_path)  # 紀錄被修改的檔案名稱
                    file_content = file_content.replace(search_text, replace_text)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(file_content)
    return modified_files

def main():
    parser = argparse.ArgumentParser(description='Search and replace text in files within a directory.')
    parser.add_argument('folder_path', type=str, help='The path to the folder to search in.')
    parser.add_argument('search_text', type=str, help='The text to search for.')
    parser.add_argument('replace_text', type=str, help='The text to replace with.')
    parser.add_argument('--exclude_dirs', nargs='+', default=None, help='Directories to exclude.')
    args = parser.parse_args()

    folder_path = args.folder_path
    search_text = args.search_text
    replace_text = args.replace_text
    exclude_dirs = args.exclude_dirs
    print(folder_path, search_text, replace_text, exclude_dirs)

    modified_files = replace_text_in_files(folder_path, search_text, replace_text, exclude_dirs)

    # 列印被修改的檔案名稱
    print("以下檔案已被修改：")
    for file_path in modified_files:
        print(file_path)

if __name__ == "__main__":
    main()

