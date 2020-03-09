from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH


class Mp3TaggerManager():
    def open_mp3_file(self, path):
        return MP3File(path)

    def read_version_tags(self, version, mp3_file):
        if (version == 1):
            mp3_file.set_version(VERSION_1)
        else:
            mp3_file.set_version(VERSION_2)

        tags = {
            'artist': mp3_file.artist,
            'song': mp3_file.song,
        }

        return tags

    def write_artist_and_song_tags(self, file, tags):
        file.artist = tags.get('artist', '')
        file.song = tags.get('song', '')
        file.save()

        return file
