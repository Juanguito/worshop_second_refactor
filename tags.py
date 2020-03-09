# from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import os

from mp3_tagger_manager import Mp3TaggerManager

class Tags():
    def __init__(self):
        self.manager = Mp3TaggerManager()

    def open_mp3_file(self, path):
        return self.manager.open_mp3_file(path)

    def read_tags(self, mp3_file):
        tags = self.manager.read_version_tags(2, mp3_file)

        if not tags.get('artist', False) or not tags.get('song', False):
            tags = self.manager.read_version_tags(1, mp3_file)

        return tags

    def get_artist_and_song_from_file_name(self, file):
        file_name = os.path.splitext(file.name)[0]
        clear_file_name = file_name.replace('_', ' ')
        tags = clear_file_name.split('-')

        return {
            'artist': tags[0],
            'song': tags[1],
        } if len(tags) == 2 else None

    def write_artist_and_song_tags(self, file, tags):
        self.manager.write_artist_and_song_tags(file, tags)

        return file
