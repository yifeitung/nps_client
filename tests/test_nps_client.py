from nps_client import __version__
from nps_client import nationalparks
import os
import pytest

api_key = os.getenv('NPS_API_KEY')


def test_version():
    assert __version__ == '0.1.0'


class TestNPS():
    def test_get_query_params(self):
        self.params = nationalparks.NPS(api_key).get_query_params()
        assert isinstance(self.params, dict)

    def test_get_categories_of_activites(self):
        self.activities = nationalparks.NPS(
            api_key).get_categories_of_activities()
        assert isinstance(self.activities, dict)

    def test_get_park_information(self):
        self.park_information = nationalparks.NPS(
            api_key).get_park_information()
        assert isinstance(self.park_information, dict)

    def test_get_vistorcenters(self):
        self.vistorcenters = nationalparks.NPS(api_key).get_vistorcenters()
        assert isinstance(self.vistorcenters, dict)

    def test_get_campgrounds(self):
        self.campgrounds = nationalparks.NPS(api_key).get_campgrounds()
        assert isinstance(self.campgrounds, dict)

    def test_get_categories_of_topics(self):
        self.topics = nationalparks.NPS(api_key).get_categories_of_topics()
        assert isinstance(self.topics, dict)

    def test_get_topics_related_parks(self):
        self.topics_parks = nationalparks.NPS(
            api_key).get_topics_related_parks()
        assert isinstance(self.topics_parks, dict)

    def test_get_amenities_types(self):
        self.amenities_types = nationalparks.NPS(api_key).get_amenities_types()
        assert isinstance(self.amenities_types, dict)

    def test_get_amentities_places_within_parks(self):
        self.amenities_places = nationalparks.NPS(
            api_key).get_amenities_places_within_parks(parkcode="acad")
        assert isinstance(self.amenities_places, dict)

    def test_api_error(self):
        with pytest.raises(Exception) as exception:
            nationalparks.NPS('123456789').get_park_information()
        assert str(
            exception.value) == "Something went wrong."
