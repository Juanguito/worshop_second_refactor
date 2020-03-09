import os
import shutil

class OsManager():
    def get_entities(self, path):
        return os.scandir(path)

    def exists(self, path):
        return os.path.exists(path)

    def join(self, path1, path2):
        return os.path.join(path1, path2)

    def create_dir(self, path):
        os.mkdir(path)

    def copy(self, source, destination):
        return shutil.copy(source, destination)

    def remove_dir(self, path):
        return shutil.rmtree(path, ignore_errors=True)
