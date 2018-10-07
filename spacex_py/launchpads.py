from ._helpers._api import _get

def get_launchpads(method=""):
    """Gets information related to launchpads used for SpaceX flights

        Gets information related to launchpads
        from the API

    Parameters
    ----------
        method : str (optional)
            the method used for the request

    Returns
    -------
        list
            a list of the launchpads
    """
    return _get("launchpads", method)