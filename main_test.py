from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from mp3_tagger.exceptions import MP3OpenFileError

from pathlib import Path
import os
import shutil
from unittest import TestCase
from unittest.mock import Mock, MagicMock

from main import MainProgram

class TestMain(TestCase):
    destination_folder = Path('./result/')

    def test_main_generates_right_mp3_file(self):
        
        main = MainProgram()
        main.retag_files()

        self.assertTrue(os.path.exists(self.destination_folder))

        complete_path = os.path.join(self.destination_folder, 'Play.mp3')
        self.assertTrue(os.path.exists(complete_path))

        mp3_file = MP3File(complete_path)
        self.assertEqual('Jax-jones-years-years', mp3_file.artist)
        self.assertEqual('Play', mp3_file.song)

    def tearDown(self):
        self.destination_folder = Path('./result/')
        if os.path.exists(self.destination_folder):
            shutil.rmtree(self.destination_folder, ignore_errors=True)
