class MusicAlbum:
    def __init__(
        self, band, title, year) -> None:
        self.set_album(band, title, year)

    def set_album(self, band, title, year) -> None:
        self.band = band
        self.title = title
        self.year = year

    def __str__(self) -> str:
            return f"Album {self.title} by {self.band}, released in {self.year}."
