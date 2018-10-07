from ._helpers._api import _get

def get_rockets(method=""):
    """Gets information related to SpaceX rockets

        Gets information related to rockets from
        the API

    Parameters
    ----------
        method : str (optional)
            the method used for the request

    Returns
    -------
        list
            a list of the rockets
    """
    return _get("rockets", method)