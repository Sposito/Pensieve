#!/usr/bin/env python3

import os
import re

class Validator:
    def __init__(self):
        self.ct = 0
        self.error_count = 0
        self.error_messages = []
        self.tests = []
        self.ERROR: str = "\033[91m[ERROR]\033[0m"
        self.target_formats = ['.md']
        self.markdown_files = dict()
        self.empty_files = []

        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith(tuple(self.target_formats)):
                    full_path = os.path.join(root, file)
                    self.markdown_files[full_path] = ""

        for path in self.markdown_files:
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.markdown_files[path] = content
                if content.strip() == "":
                    self.empty_files.append(path)
            except Exception as e:
                print(f"{self.ERROR} Could not read file {path}: {e}")

        # Register tests
        self.tests.append(self.check_empty_files)
        self.tests.append(self.check_file_name)

    def check_empty_files(self):
        if self.empty_files:
            err_msg = f"{self.ERROR} Empty files found:\n" + ''.join(f"\t[empty_file]\t{x}\n" for x in self.empty_files)
            raise AssertionError(err_msg)

    def check_file_name(self):
        for k in self.markdown_files.keys():
            filename = os.path.basename(k)
            if not re.match(r'^[a-z0-9_\-\u4e00-\u9fff]+\.md$', filename):
                raise AssertionError(f"{self.ERROR} Invalid file name: {filename}")

if __name__ == "__main__":
    v = Validator()
    for test in v.tests:
        try:
            test()
        except AssertionError as e:
            print(e)
