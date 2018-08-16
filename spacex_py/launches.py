from ._helpers._api import _get

# Launches
def get_launches(method="", **query):
    return _get("launches", method, query)

def get_past_launches(**query):
    return _get("launches", "", query)

def get_latest_launch(**query):
    return _get("launches", "latest", query)

def get_next_launch(**query):
    return _get("launches", "next", query)

def get_upcoming_launches(**query):
    return _get("launches", "upcoming", query)