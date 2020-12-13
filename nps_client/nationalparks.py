import requests


class NPS():
    """
    This is a class for making HTTP requests for National Park Service API.

    Parameters
    ----------
    API_KEY: str
        a string that you get from National Park Service Developer portal.
    """

    def __init__(self, API_KEY):
        self.base_url = "https://developer.nps.gov/api/v1"
        self.API_KEY = API_KEY

    def get_query_params(self, payload={}):
        """
        Generate a set of query parameters to authenticate a request.

        Parameters
        ----------
        payload: dict
            A dictionary that includes query parameters. Must pass apikey
            parameter. The default values include apikey and limit. The limit
            is set to 100.

        Returns
        -------
        dict
            A dictionary that includes baisc query parameters.
        """
        payload['api_key'] = self.API_KEY
        payload['limit'] = 100
        return payload

    def get_categories_of_activities(self, payload=None):
        """
        Retrieve categories of activities (astronomy, hiking, wildlife watching
        , etc.) possible in national parks.

        Parameters
        ----------
        payload: dict
            A dictionary that includes query parameters. This parameter is not
            necessary. But you could include additional parameters. For
            example, if you want to search some activities, you can pass q
            into parameters.

        Returns
        -------
        dict
        """
        if payload is None:
            payload = {}
        url = self.base_url + "/activities"
        query = self.get_query_params(payload=payload)
        response = requests.get(url, params=query)
        status_code = response.status_code
        if status_code != 200:
            raise Exception("Something went wrong.")
        else:
            return response.json()

    def get_park_information(self, parkcode=None, statecode=None,
                             start=None, q=""):
        """
        Retrieve data about national parks (address, contacts, description,
        hours of operation, etc)

        Parameters
        ----------
        parkcode: str
            A comma delimited list of park codes (each 4-10 characters in
            length).
        statecode: str
            A comma delimited list of 2 character state codes.
        start: int
            Get the next 100 results starting with this number. Deafult is 0.
        q: str
            Term to search on

        Returns
        -------
        dict
        """
        payload = {}
        url = self.base_url + "/parks"
        if start is None:
            payload['start'] = 0
        if not (start is None):
            try:
                if isinstance(start, (str, float)):
                    raise TypeError
                if start < 0:
                    raise ValueError
            except (TypeError, ValueError):
                print('Please check your input values for start.')
                return None
            else:
                payload['start'] = start
        if not (parkcode is None):
            payload.update({'parkCode': parkcode})
        if not (statecode is None):
            payload.update({'stateCode': statecode})
        if q == "":
            pass
        else:
            payload.update({'q': q})
        query = self.get_query_params(payload=payload)
        response = requests.get(url, params=query)
        status_code = response.status_code
        if status_code != 200:
            raise Exception("Something went wrong.")
        else:
            return response.json()

    def get_vistorcenters(self, parkcode=None, statecode=None,
                          start=None, q=""):
        """
        Retrieve data about National Park Service visitor centers including
        addresses, contacts, description, hours of operation, etc.

        Parameters
        ----------
        parkcode: str
            A comma delimited list of park codes (each 4 characters in length).
        statecode: str
            A comma delimited list of 2 character state codes.
        start: int
            Get the next 100 results starting with this number. Deafult is 0.
        q: str
            Term to search on

        Returns
        -------
        dict
        """
        payload = {}
        url = self.base_url + "/visitorcenters"
        if start is None:
            payload['start'] = 0
        if not (start is None):
            try:
                if isinstance(start, (str, float)):
                    raise TypeError
                if start < 0:
                    raise ValueError
            except (TypeError, ValueError):
                print('Please check your input values for start.')
                return None
            else:
                payload['start'] = start
        if not (parkcode is None):
            payload.update({'parkCode': parkcode})
        if not (statecode is None):
            payload.update({'statecode': statecode})
        if q == "":
            pass
        else:
            payload.update({'q': q})
        query = self.get_query_params(payload=payload)
        response = requests.get(url, params=query)
        status_code = response.status_code
        if status_code != 200:
            raise Exception("Something went wrong.")
        else:
            return response.json()

    def get_campgrounds(self, parkcode=None, statecode=None,
                        start=None, q=""):
        """
        Retrieve data about National Park Service campgrounds including
        addresses, contacts, description, hours of operation, etc.

        Parameters
        ----------
        parkcode: str
            A comma delimited list of park codes (each 4 characters in length).
        statecode: str
            A comma delimited list of 2 character state codes.
        start: int
            Get the next 100 results starting with this number. Deafult is 0.
        q: str
            Term to search on

        Returns
        -------
        dict
        """
        payload = {}
        url = self.base_url + '/campgrounds'
        if not (start is None):
            payload['start'] = start
        else:
            payload['start'] = 0
        if not (parkcode is None):
            payload.update({'parkCode': parkcode})
        if not (statecode is None):
            payload.update({'stateCode': statecode})
        if q == "":
            pass
        else:
            payload.update({'q': q})
        query = self.get_query_params(payload=payload)
        response = requests.get(url, params=query)
        status_code = response.status_code
        if status_code != 200:
            raise Exception("Something went wrong.")
        else:
            return response.json()

    def get_categories_of_topics(self, id="", q="", start=None):
        """
        Retrieve categories of topics (American revolution, music, women's
        history, etc.) relating to national parks.

        Parameters
        ----------
        id: str
            Topic ID.
        q: str
            A string to search for.
        start: int
            Get the next 100 results starting with this number. Deafult is 0 if
            you do not sepecify.

        Returns
        -------
        dict
        """
        payload = {}
        url = self.base_url + "/topics"
        if start is None:
            payload['start'] = 0
        if not (start is None):
            try:
                if isinstance(start, (str, float)):
                    raise TypeError
                if start < 0:
                    raise ValueError
            except (TypeError, ValueError):
                print('Please check your input values for start.')
                return None
            else:
                payload['start'] = start
        if id == "":
            pass
        else:
            payload.update({'id': id})
        if q == "":
            pass
        else:
            payload.update({'q': q})
        query = self.get_query_params(payload)
        response = requests.get(url, params=query)
        status_code = response.status_code
        if status_code != 200:
            raise Exception("Something went wrong.")
        else:
            return response.json()

    def get_topics_related_parks(self, id="", q="", start=None):
        """
        Retrieve national parks taht are related to particular categories of
        topics (American revolution, music, women's history, etc.)

        Parameters
        ----------
        id: str
            Topic ID.
        q: str
            A string to search for.
        start: int
            Get the next 100 results starting with this number. Default is 0 if
            you do not specify.

        Returns
        -------
        dict
        """
        payload = {}
        url = self.base_url + "/topics/parks"
        if start is None:
            payload['start'] = 0
        if not (start is None):
            try:
                if isinstance(start, (str, float)):
                    raise TypeError
                if start < 0:
                    raise ValueError
            except (TypeError, ValueError):
                print("Please check your input values for start.")
                return None
            else:
                payload['start'] = start
        if id == "":
            pass
        else:
            payload.update({'id': id})
        if q == "":
            pass
        else:
            payload.update({'q': q})
        query = self.get_query_params(payload)
        response = requests.get(url, params=query)
        status_code = response.status_code
        if status_code != 200:
            raise Exception("Something went wrong.")
        else:
            return response.json()

    def get_amenities_types(self, id="", q="", start=None):
        """
        Retrieve the amenity types (accessible restrooms, fire pit, picnic
        area, etc.) available in national parks.

        Parameters
        ----------
        id: str
            Topic unique ID.
        q: str
            A string to search for.
        start: int
            Get the next 100 results starting with this number. Default is 0 if
            you do not specify.

        Returns
        -------
        dict
        """
        payload = {}
        url = self.base_url + "/amenities"
        if start is None:
            payload['start'] = 0
        if not (start is None):
            try:
                if isinstance(start, (str, float)):
                    raise TypeError
                if start < 0:
                    raise ValueError
            except (TypeError, ValueError):
                print("Please check your input values for start.")
                return None
            else:
                payload['start'] = start
        if id == "":
            pass
        else:
            payload.update({'id': id})
        if q == "":
            pass
        else:
            payload.update({'q': q})
        query = self.get_query_params(payload=payload)
        response = requests.get(url, params=query)
        status_code = response.status_code
        if status_code != 200:
            raise Exception("Something went wrong.")
        else:
            return response.json()

    def get_amenities_places_within_parks(self, parkcode=None,
                                          id="", q="", start=None):
        """
        Retrieve "places" within national parks that have different amenities.

        Parameters
        ----------
        parkcode: str
            4 character park code.
        id: str
            Amenity ID.
        q: str
            A string to search for.
        start: int
            Get the next 100 results starting with this number. Deafult is 0 if
            you do not specify.

        Returns
        -------
        dict
        """
        payload = {}
        url = self.base_url + "/amenities/parksplaces"
        if start is None:
            payload['start'] = 0
        else:
            try:
                if isinstance(start, (str, float)):
                    raise TypeError
                if start < 0:
                    raise ValueError
            except (TypeError, ValueError):
                print("Plase check your input values for start.")
                return None
            else:
                payload['start'] = start
        if id == "":
            pass
        else:
            payload.update({'id': id})
        if q == "":
            pass
        else:
            payload.update({'q': q})
        if not (parkcode is None):
            payload.update({'parkCode': parkcode})
        query = self.get_query_params(payload=payload)
        response = requests.get(url, params=query)
        status_code = response.status_code
        if status_code != 200:
            raise Exception("Something went wrong.")
        else:
            return response.json()
