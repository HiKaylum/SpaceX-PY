from ._helpers._api import _get

def get_rockets(method=""):
    return _get("rockets", method)