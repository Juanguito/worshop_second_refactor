from pathlib import Path
import shutil
from unittest import TestCase

import os_manager

class OSManager(TestCase):
    os = os_manager.OsManager()

    def escape_path(self, path):
        return str(Path(path))

    def setUp(self):
        pass

    def test_list_not_valid_path_raises_exception(self):
        with self.assertRaises(Exception):
            self.os.get_entities(self.escape_path('./foo'))

    def test_list_directories_and_files(self):
        entities = self.os.get_entities(self.escape_path('./test'))

        assert entities
        assert len(list(entities)) == 2

    def test_not_existing_path_returns_false(self):
        assert not self.os.exists(self.escape_path('./foo'))

    def test_existing_path_returns_true(self):
        assert self.os.exists(self.escape_path('./test/bar.txt'))

    def test_join_path_with_none_raises_exception(self):
        with self.assertRaises(Exception):
            self.os.join(self.escape_path('./foo'), None)

    def test_join_paths_returns_complete_path(self):
        complete_path = self.os.join(self.escape_path('./foo'), 'bar.txt')

        assert complete_path == self.escape_path('./foo/bar.txt')

    def test_create_dir_from_None_raises_exception(self):
        with self.assertRaises(Exception):
            self.os.create_dir(None)

    def test_create_dir_creates_new_dir(self):
        folder_path = self.escape_path('./foo')

        assert not self.os.exists(folder_path)
        self.os.create_dir(folder_path)
        assert self.os.exists(folder_path)

    def test_copy_not_existing_source_raises_exception(self):
        with self.assertRaises(FileNotFoundError):
            self.os.copy(
                self.escape_path('bar.txt'),
                self.escape_path('./test/foo/bar.txt'),
            )

    def test_copy_file_to_destination(self):
        source = self.escape_path('./test/bar.txt')
        destination = self.escape_path('./test/foo/bar.txt')

        new_path = self.os.copy(source, destination)

        assert new_path
        assert new_path == destination


    def tearDown(self):
        folder_path = self.escape_path('./foo')
        if self.os.exists(folder_path):
            shutil.rmtree(folder_path, ignore_errors=True)

        destination_file = self.escape_path('./test/foo/bar.txt')
        if self.os.exists(destination_file):
            shutil.rmtree(destination_file, ignore_errors=True)
