#!/usr/bin/env python3

import os
import re
import urllib.parse

def assert_test(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except AssertionError as e:
            print(e)
            return False
    return wrapper

class Validator:
    def __init__(self):
        self.ct = 0
        self.error_count = 0
        self.error_messages = []
        self.ERROR = "\033[91m[ERROR]\033[0m"
        self.target_formats = ['.md']
        self.markdown_files = {}
        self.empty_files = []

        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith(tuple(self.target_formats)):
                    self.markdown_files[os.path.join(root, file)] = ""

        for path in list(self.markdown_files):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.markdown_files[path] = content
            if content.strip() == "":
                self.empty_files.append(path)

        self.tests = [
            self.check_empty_files,
            self.check_file_name,
        ]

    @assert_test
    def check_empty_files(self):
        err_msg = (
            f"{self.ERROR} Empty files found:\n"
            + ''.join(f"\t[empty_file]\t{x}\n" for x in self.empty_files)
        )
        assert not self.empty_files, err_msg

    @assert_test
    def check_file_name(self):
        for path in self.markdown_files:
            filename = os.path.basename(path)
            name, _ = os.path.splitext(filename)
            assert re.match(r'^[a-z0-9_\-\u4e00-\u9fff]+$', name), \
                f"{self.ERROR} Invalid file name://{urllib.parse.quote(os.path.abspath(path))}"

if __name__ == "__main__":
    v = Validator()
    for test in v.tests:
        test()
