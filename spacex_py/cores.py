from ._helpers._api import _get

def get_cores(method="", **query):
    """Gets all core parts based on query strings

        Gets all core parts based on query strings
        from the API

    Parameters
    ----------
        method : str (optional)
            the method used for the request
        query : keyword args
            keyword args based on the API query strings

    Returns
    -------
        list
            a list of the core parts
    """
    return _get("parts/cores", method, query)