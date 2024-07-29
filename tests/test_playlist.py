import pytest
from app.playlist import Playlist
from app.track import Track

def test_playlist_creation():
    playlist = Playlist(1, 123, 'My Playlist')
    assert playlist.id == 1
    assert playlist.user_id == 123
    assert playlist.name == 'My Playlist'
    assert playlist.tracks == []

def test_add_track():
    playlist = Playlist(1, 123, 'My Playlist')
    track = Track(1, 'Hypnotized', 'Purple Disco Machine', 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2')
    playlist.add_track(track.id)
    assert len(playlist.tracks) == 1
    assert playlist.tracks[0] == track.id

def test_remove_track():
    track1 = Track(1, 'Hypnotized', 'Purple Disco Machine', 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2')
    track2 = Track(2, 'Aquaman', 'WALK THE MOON', 'spotify:track:71wT7aMCFPYfzutF66OLac')
    playlist = Playlist(1, 123, 'My Playlist', [track1.id, track2.id])
    playlist.remove_track(1)
    assert len(playlist.tracks) == 1
    assert playlist.tracks[0] == track2.id

def test_add_invalid_track():
    playlist = Playlist(1, 123, 'My Playlist')
    with pytest.raises(TypeError):
        playlist.add_track("Not a Track")

def test_playlist_str():
    track = Track(1, 'Hypnotized', 'Purple Disco Machine', 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2')
    playlist = Playlist(1, 123, 'My Playlist', [track.id])
    assert str(playlist) == 'Playlist ID: 1, User ID: 123, Name: "My Playlist", Tracks: [Track ID: 1]'

if __name__ == '__main__':
    pytest.main()
