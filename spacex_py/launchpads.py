from ._helpers._api import _get

def get_launchpads(method=""):
    return _get("launchpads", method)