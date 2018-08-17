from ._helpers._api import _get

def get_launches(method="", **query):
    """Gets launches based on query strings

        Gets launches based on query strings from
        the API

    Parameters
    ----------
        method : str (optional)
            the method used for the request
        query : keyword args
            keyword args based on the API query stings

    Returns
    -------
        list
            a list of the launches
    """
    return _get("launches", method, query)

def get_past_launches(**query):
    """Gets past launches

    Parameters
    ----------
        query : keyword args
            keyword args based on the API query strings
    
    Returns
    -------
        list
            a list of previous launches
    """
    return _get("launches", "", query)

def get_latest_launch(**query):
    """Gets the latest launch

    Parameters
    ----------
        query : keyword args
            keyword args based on the API query strings
    
    Returns
    -------
        dict
            a dict containing latest launch data
    """
    return _get("launches", "latest", query)

def get_next_launch(**query):
    """Gets the next launch

    Parameters
    ----------
        query : keyword args
            keyword args based on the API query strings
    
    Returns
    -------
        dict
            a dict containing next launch data
    """
    return _get("launches", "next", query)

def get_upcoming_launches(**query):
    """Gets upcoming launches

    Parameters
    ----------
        query : keyword args
            keyword args based on the API query strings

    Retunrs
    -------
        list
            a list of the upcoming launches
    """
    return _get("launches", "upcoming", query)