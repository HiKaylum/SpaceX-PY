from ._helpers._api import _get

def get_cores(method="", **query):
    return _get("parts/cores", method, query)