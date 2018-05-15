import os


class Search:
    def __init__(self, directory):
        self.directory = directory

    def do_search(self, query):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith(query[1:]):
                    path_file = os.path.join(root, file)
                    size = os.path.getsize(path_file)
                    file = File(path_file, size)
                    yield file


class File:
    def __init__(self, path, size):
        self.path = path
        self.size = size

    def __str__(self):
        return "file " + self.path + " size " + str(self.size)

    def __add__(self, number):
        self.size += number

    def __getitem__(self, key):
        if key == "name":
            return self.path
