class Playlist:
    def __init__(self, id, user_id, name, tracks=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.tracks = tracks if tracks is not None else []

    def __str__(self):
        track_list = ', '.join([f'Track ID: {tid}' for tid in self.tracks])
        return f'Playlist ID: {self.id}, User ID: {self.user_id}, Name: "{self.name}", Tracks: [{track_list}]'