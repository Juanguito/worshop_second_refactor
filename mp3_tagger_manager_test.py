from pathlib import Path
from unittest import TestCase
from unittest.mock import (
    Mock,
    MagicMock,
)

import folders
from mp3_tagger_manager import Mp3TaggerManager


class TestMp3TaggerManager(TestCase):
    folder_manager = folders.Folders()
    tagger_manager = Mp3TaggerManager()

    def test_cant_open_file_as_mp3(self):
        if not self.folder_manager.exists('filename.txt'):
            file = open('filename.txt','w+')
            file.close()

        not_mp3_file_path = Path('./filename.txt')

        with self.assertRaises(Exception):
            self.tagger_manager.open_mp3_file(not_mp3_file_path)

    def test_can_open_file_as_mp3(self):
        mp3_file_source_path = Path('./files/jax-jones-years-years-play.mp3')

        assert self.tagger_manager.open_mp3_file(str(mp3_file_source_path))

    def test_read_version_1_tags(self):
        mock_file = Mock(artist='artist', song='song')

        tags = self.tagger_manager.read_version_tags(1, mock_file)

        self.assertEqual('artist', tags['artist'])
        self.assertEqual('song', tags['song'])

    def test_read_version_2_tags(self):
        mock_file = Mock(artist='artist', song='song')

        tags = self.tagger_manager.read_version_tags(2, mock_file)

        self.assertEqual('artist', tags['artist'])
        self.assertEqual('song', tags['song'])


    def tearDown(self):
        if self.folder_manager.exists('filename.txt'):
            self.folder_manager.remove_dir('filename.txt')
