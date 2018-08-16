import requests

def _get(endpoint, method, query={}):
    """GET request to the SpaceX API

        Sends HTTP request to the SpaceX API given a
        set of parameters. Should only be used by the
        spacex_py module

    Parameters
    ----------
        endpoint : str
            The endpoint for the request
        method : str
            The method used for the request
        query : dict
            A dictionary representation of query string options

    Returns
    -------
        tuple
            returns the response body and headers
    """
    request_url = "https://api.spacexdata.com/v2/{end}/{meth}".format(
        end=endpoint, meth=method)
    res = requests.get(request_url, params=query)

    if not res.ok:
        res.raise_for_status()

    return res.json(), res.headers
