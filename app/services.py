import requests
from core.settings import LAST_FM_API_KEY
from abc import ABC, abstractmethod


class GetDataExternalAPI(ABC):
    """base abstract class got get data"""

    ...


class GetDataFmApi(GetDataExternalAPI):
    """abstract class for last.fm Apis"""

    ...


class GetFMAlbumData(GetDataFmApi):
    def fetch_data_album(album):
        """function to fetch data from last.fm apis"""
        try:
            response = requests.get(
                f"http://ws.audioscrobbler.com/2.0/?method=album.search&album={album}&api_key={LAST_FM_API_KEY}&format=json"
            )
            if response.status_code == 200:
                # adding hardcoded key name to get album data
                return response.json()

        except Exception as e:
            return str(e)


class FilterAlbumData(GetDataFmApi):
    def get_first_values(data):
        """function to filter out response json to get required first record details
        params:
            data:json response
        """
        response_data = dict()
        album_data = data["results"]["albummatches"]["album"][0]
        response_data.update(
            {"album": album_data["name"], "artist": album_data["artist"]}
        )

        return response_data
