#   MIT License
#   Copyright (c) 2021. Plato Puthur

import json
import os


class FileManager:

    @staticmethod
    def read_file(filepath):
        file_content = None
        with open(filepath) as f:
            file_content = f.read()
        return file_content
