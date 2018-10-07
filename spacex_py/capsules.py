from ._helpers._api import _get

def get_capsules(method=""):
    """Gets all capsules

        Gets capsules from the API

    Parameters
    ----------
        method : str (optional)
            the method used for the request

    Returns
    -------
        list
            a list of capsules
    """
    return _get("capsules", method)

def get_capsule_parts(method="", **query):
    """Gets all capsule parts based on query strings

        Gets all capsule parts based on query strings
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
            a list of the capsule parts
    """
    return _get("parts/caps", method, query)