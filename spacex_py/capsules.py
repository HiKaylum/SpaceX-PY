from ._helpers._api import _get

def get_capsules(method=""):
    return _get("capsules", method)

def get_capsule_parts(method="", **query):
    return _get("parts/caps", method, query)