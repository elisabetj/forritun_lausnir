import unittest

from music_album import MusicAlbum


NO_BAND = "unknown band"
NO_TITLE = "unknown"
NO_YEAR = "unknown year"


class MusicAlbumConstructorUnitTests(unittest.TestCase):
    """
    Test case 1 (1. Constructor):
    """

    def test_all_parameters_provided(self):
        # Arrange
        input_band = "Talking Heads"
        input_title = "Remain in Light"
        input_year = 1980

        expected_band = input_band
        expected_title = input_title
        expected_year = input_year

        # Act
        album = MusicAlbum(band=input_band, title=input_title, year=input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_no_parameters_provided(self):
        # Arrange
        expected_band = NO_BAND
        expected_title = NO_TITLE
        expected_year = NO_YEAR

        # Act
        album = MusicAlbum()
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_band_provided(self):
        # Arrange
        input_band = "Talking Heads"

        expected_band = input_band
        expected_title = NO_TITLE
        expected_year = NO_YEAR

        # Act
        album = MusicAlbum(band=input_band)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_title_provided(self):
        # Arrange
        input_title = "Remain in Light"

        expected_band = NO_BAND
        expected_title = input_title
        expected_year = NO_YEAR

        # Act
        album = MusicAlbum(title=input_title)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_year_provided(self):
        # Arrange
        input_year = 1980

        expected_band = NO_BAND
        expected_title = NO_TITLE
        expected_year = input_year

        # Act
        album = MusicAlbum(year=input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_no_band_provided(self):
        # Arrange
        input_title = "Remain in Light"
        input_year = 1980

        expected_band = NO_BAND
        expected_title = input_title
        expected_year = input_year

        # Act
        album = MusicAlbum(title=input_title, year=input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_no_title_provided(self):
        # Arrange
        input_band = "Talking Heads"
        input_year = 1980

        expected_band = input_band
        expected_title = NO_TITLE
        expected_year = input_year

        # Act
        album = MusicAlbum(band=input_band, year=input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_no_year_provided(self):
        # Arrange
        input_band = "Talking Heads"
        input_title = "Remain in Light"

        expected_band = input_band
        expected_title = input_title
        expected_year = NO_YEAR

        # Act
        album = MusicAlbum(band=input_band, title=input_title)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)


class MusicAlbumSetAlbumUnitTests(unittest.TestCase):
    """
    Test case 2 (2. set_album()):
    """

    def test_all_parameters_provided(self):
        # Arrange
        album = MusicAlbum("Madeon", "Good Faith", 2019)

        input_band = "Talking Heads"
        input_title = "Remain in Light"
        input_year = 1980

        expected_band = input_band
        expected_title = input_title
        expected_year = input_year

        # Act
        album.set_album(band=input_band, title=input_title, year=input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_no_parameters_provided(self):
        # Arrange
        album = MusicAlbum("Madeon", "Good Faith", 2019)

        expected_band = NO_BAND
        expected_title = NO_TITLE
        expected_year = NO_YEAR

        # Act
        album.set_album()
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_band_provided(self):
        # Arrange
        album = MusicAlbum("Madeon", "Good Faith", 2019)

        input_band = "Talking Heads"

        expected_band = input_band
        expected_title = NO_TITLE
        expected_year = NO_YEAR

        # Act
        album.set_album(band=input_band)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_title_provided(self):
        # Arrange
        album = MusicAlbum("Madeon", "Good Faith", 2019)

        input_title = "Remain in Light"

        expected_band = NO_BAND
        expected_title = input_title
        expected_year = NO_YEAR

        # Act
        album.set_album(title=input_title)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_year_provided(self):
        # Arrange
        album = MusicAlbum("Madeon", "Good Faith", 2019)

        input_year = 1980

        expected_band = NO_BAND
        expected_title = NO_TITLE
        expected_year = input_year

        # Act
        album.set_album(year=input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_no_band_provided(self):
        # Arrange
        album = MusicAlbum("Madeon", "Good Faith", 2019)

        input_title = "Remain in Light"
        input_year = 1980

        expected_band = NO_BAND
        expected_title = input_title
        expected_year = input_year

        # Act
        album.set_album(title=input_title, year=input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_no_title_provided(self):
        # Arrange
        album = MusicAlbum("Madeon", "Good Faith", 2019)

        input_band = "Talking Heads"
        input_year = 1980

        expected_band = input_band
        expected_title = NO_TITLE
        expected_year = input_year

        # Act
        album.set_album(band=input_band, year=input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

    def test_no_year_provided(self):
        # Arrange
        album = MusicAlbum("Madeon", "Good Faith", 2019)

        input_band = "Talking Heads"
        input_title = "Remain in Light"

        expected_band = input_band
        expected_title = input_title
        expected_year = NO_YEAR

        # Act
        album.set_album(band=input_band, title=input_title)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)


class MusicAlbumStringUnitTests(unittest.TestCase):
    """
    Test case 3 (3. String):
    """

    def test_all_parameters_provided(self):
        # Arrange
        input_band = "Talking Heads"
        input_title = "Remain in Light"
        input_year = 1980
        album = MusicAlbum(band=input_band, title=input_title, year=input_year)

        expected_band = input_band
        expected_title = input_title
        expected_year = input_year
        expected = (
            f"Album {expected_title} by {expected_band}, released in {expected_year}."
        )

        # Act
        actual = str(album)

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_no_parameters_provided(self):
        # Arrange
        album = MusicAlbum()

        expected_band = NO_BAND
        expected_title = NO_TITLE
        expected_year = NO_YEAR
        expected = (
            f"Album {expected_title} by {expected_band}, released in {expected_year}."
        )

        # Act
        actual = str(album)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_band_provided(self):
        # Arrange
        input_band = "Talking Heads"
        album = MusicAlbum(band=input_band)

        expected_band = input_band
        expected_title = NO_TITLE
        expected_year = NO_YEAR
        expected = (
            f"Album {expected_title} by {expected_band}, released in {expected_year}."
        )

        # Act
        actual = str(album)

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_title_provided(self):
        # Arrange
        input_title = "Remain in Light"
        album = MusicAlbum(title=input_title)

        expected_band = NO_BAND
        expected_title = input_title
        expected_year = NO_YEAR
        expected = (
            f"Album {expected_title} by {expected_band}, released in {expected_year}."
        )

        # Act
        actual = str(album)

        # Assert
        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_year_provided(self):
        # Arrange
        input_year = 1980
        album = MusicAlbum(year=input_year)

        expected_band = NO_BAND
        expected_title = NO_TITLE
        expected_year = input_year
        expected = (
            f"Album {expected_title} by {expected_band}, released in {expected_year}."
        )

        # Act
        actual = str(album)

        # Assert
        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_no_band_provided(self):
        # Arrange
        input_title = "Remain in Light"
        input_year = 1980
        album = MusicAlbum(title=input_title, year=input_year)

        expected_band = NO_BAND
        expected_title = input_title
        expected_year = input_year
        expected = (
            f"Album {expected_title} by {expected_band}, released in {expected_year}."
        )

        # Act
        actual = str(album)

        # Assert
        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_no_title_provided(self):
        # Arrange
        input_band = "Talking Heads"
        input_year = 1980
        album = MusicAlbum(band=input_band, year=input_year)

        expected_band = input_band
        expected_title = NO_TITLE
        expected_year = input_year
        expected = (
            f"Album {expected_title} by {expected_band}, released in {expected_year}."
        )

        # Act
        actual = str(album)

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_no_year_provided(self):
        # Arrange
        input_band = "Talking Heads"
        input_title = "Remain in Light"
        album = MusicAlbum(band=input_band, title=input_title)

        expected_band = input_band
        expected_title = input_title
        expected_year = NO_YEAR
        expected = (
            f"Album {expected_title} by {expected_band}, released in {expected_year}."
        )

        # Act
        actual = str(album)

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()


"""
template:


class MusicAlbumUnitTests(unittest.TestCase):
    def test_all_parameters_provided(self):
        # Arrange
        input_band = "Talking Heads"
        input_title = "Remain in Light"
        input_year = 1980

        expected_band = input_band
        expected_title = input_title
        expected_year = input_year

        # Act
        album = MusicAlbum(input_band, input_title, input_year)
        actual_band = album.band
        actual_title = album.title
        actual_year = album.year

        # Assert
        message = f"\n\nInput band ({type(input_band)}):\n{input_band}"
        message += f"\n\nExpected band ({type(expected_band)}):\n{expected_band}"
        message += f"\n\nActual band ({type(actual_band)}):\n{actual_band}"
        self.assertEqual(expected_band, actual_band, message)

        message = f"\n\nInput title ({type(input_title)}):\n{input_title}"
        message += f"\n\nExpected title ({type(expected_title)}):\n{expected_title}"
        message += f"\n\nActual title ({type(actual_title)}):\n{actual_title}"
        self.assertEqual(expected_title, actual_title, message)

        message = f"\n\nInput year ({type(input_year)}):\n{input_year}"
        message += f"\n\nExpected year ({type(expected_year)}):\n{expected_year}"
        message += f"\n\nActual year ({type(actual_year)}):\n{actual_year}"
        self.assertEqual(expected_year, actual_year, message)

"""
