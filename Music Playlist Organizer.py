class MusicPlaylist:
    def __init__(self):
        self.playlist = []

    def add_song(self, title, artist, genre):
        song = {
            'title': title,
            'artist': artist,
            'genre': genre,
        }
        self.playlist.append(song)
        print(f"Added '{title}' by {artist} to the playlist")

    def display_playlist(self):
        if not self.playlist:
            print("Playlist is empty")
        else:
            print("\nPlaylist:")
            for index, song in enumerate(self.playlist, start=1):
                print(f"{index} {song['title']} by {song['artist']} ({song['genre']})")
    def remove_song(self, title):
        for song in self.playlist:
            if song['title'] == title:
                self.playlist.remove(song)
                print(f"Remove '{title}' from the playlist")
                return
        print(f"Song '{title}' not found in the playlist")

def main():
    playlist_manager = MusicPlaylist()

    while True:
        print("\nMusic Playlist Organizer:")
        print("1. Add Song")
        print("2. Display Playlist")
        print("3. Remove Song")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter the song title: ")
            artist = input("Enter the artist: ")
            genre = input("Enter the genre: ")
            playlist_manager.add_song(title, artist, genre)

        elif choice == '2':
            playlist_manager.display_playlist()

        elif choice == '3':
            title = input("Enter the song title to remove: ")
            playlist_manager.remove_song(title)

        elif choice == '4':
            print("Exiting the Music Playlist Organizer. Goodbye!")
            break

        else:
            print("Invalid choice Please enter a number between 1 and 4")

if __name__ == "__main__":
    main()