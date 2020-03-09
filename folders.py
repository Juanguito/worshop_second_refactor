import os_manager

class Folders():
    def __init__(self):
        self.folder_manager = os_manager.OsManager()

    def retrieve_mp3_files(self, path):
        return set(
            entry for entry in self.folder_manager.get_entities(path)
            if entry.is_file() and entry.name.endswith('.mp3')
        )

    def copy_file(self, source, destination, file_name):
        if not self.folder_manager.exists(source):
            return None

        if not self.folder_manager.exists(destination):
            self.folder_manager.create_dir(destination)

        destination_file_path = self.folder_manager.join(
                destination,
                file_name,
            )

        newPath = self.folder_manager.copy(source, destination_file_path)

        return newPath

    def join(self, path_1, path_2):
        return self.folder_manager.join(path_1, path_2)
    
    def exists(self, path):
        return self.folder_manager.exists(path)

    def remove_dir(self, path):
        self.folder_manager.remove_dir(path)
